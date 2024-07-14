import sys
import json
from utils.init_camera import init_camera
from utils.calculo_rotacion import calcular_angulo_rotacion
from utils.calculate_camera_tilt import calculate_camera_tilt
from utils.calculate_zoom import calculate_zoom
from utils.scale import scale_angle_0to1, scale_angle_90degresstilt, scale_angle_less1to1, scale_angle_less1to1_90degresstilt
from utils.tilt_optimization import tilt_optimization_function

def main(json_parameters):
    data = json.loads(json_parameters)
    print(json.dumps(data, indent=4))

    for cam in data["camaras"]:
        # Extract necessary data from input
        cam_coord = tuple(map(float, cam["coordenada_camara"]))
        ref_coord = tuple(map(float, cam["coordenada_referencia"]))
        emerg_coord = tuple(map(float, data["coordenada"]))
        ref_pan = cam["origen_ptz"][0]
        altura = cam["altura"]
        scale_pan = cam["scale_pan"]
        scale_tilt = cam["scale_tilt"]
        scale_zoom = cam["scale_zoom"]
        zoom_min = cam["zoom_min"]
        zoom_max = cam["zoom_max"]
        min_tilt_optimization_distance = cam["min_tilt_optimization_distance"]
        tilt_optimization = cam["tilt_optimization"]
        
        camara = init_camera(data)
        pan, cross = calcular_angulo_rotacion(cam_coord, ref_coord, emerg_coord, ref_pan)
        print(f"Pan according to rotation in degrees: {pan}")
        if(scale_pan == '01'): pan = scale_angle_0to1(pan, ref_pan, cross)
        if(scale_pan == '-11'): pan = scale_angle_less1to1(pan , ref_pan, cross)
        print(f"Pan for camera movement: {pan}")
        if(tilt_optimization): altura = tilt_optimization_function(min_tilt_optimization_distance, tilt_optimization, altura, cam_coord, emerg_coord)
        tilt = calculate_camera_tilt(cam_coord, emerg_coord, altura)
        print(f"Tilt before scaling: {tilt}")
        if(scale_tilt == '01'): tilt = scale_angle_90degresstilt(tilt)
        if(scale_tilt == '-11'): tilt = scale_angle_less1to1_90degresstilt(tilt)
        print(f"Tilt for camera movement: {tilt}")
        zoom = calculate_zoom(cam_coord, emerg_coord, zoom_min, zoom_max)
        print(f"Calculated zoom: {zoom}")
        print(f"Moving camera to Pan: {pan}, Tilt: {tilt}, Zoom: {zoom}")
        camara.move(pan,tilt, zoom)
