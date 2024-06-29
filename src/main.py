import sys
import json
from utils.init_camera import init_camera
from utils.calculo_rotacion import calcular_angulo_rotacion
from utils.calculate_camera_tilt import calculate_camera_tilt
from utils.calculate_zoom import calculate_zoom
from utils.scale import scale_angle_0to1, scale_angle_90degresstilt, scale_angle_less1to1, scale_angle_less1to1_90degresstilt

usuario="davidvalorwork@gmail.com"
password= "14141313aA@@"
serial = "BB2643869"

json_parameters = '{ "emergencia_id": "1", "coordenada": [ 10.364744, -66.977883 ], "camaras": [ { "id": 1, "scale_pan": "01", "scale_tilt": "01", "scale_zoom": "03", "coordenada_camara": [ 10.365072129702737, -66.9775462486802 ], "coordenada_referencia": [ 10.364764751417162, -66.97756636524517 ], "altura": 45, "origen_ptz": [ 0.565, 1, 0 ], "vpn": "wg0", "ip": "10.0.0.4", "puerto": 80, "usuario": "davidvalorwork@gmail.com", "contrasena": "14141313aA@@", "serial": "BB2643869", "tipo_camara": "ezviz" } ] }'
json_parameters = '{ "emergencia_id": "1", "coordenada": [ -33.564374585967286, -70.55213001080034 ], "camaras": [ { "id": 1, "coordenada_camara": [ -33.56467351554227, -70.55168811687197 ], "coordenada_referencia": [ -33.56488416249139, -70.55192750401524 ], "altura": 3, "scale_pan": "-11", "scale_tilt": "01", "scale_zoom": "03", "origen_ptz": [ 0.143, 0.5, 0 ], "vpn": "wg0", "ip": "192.168.0.64", "puerto": 80, "usuario": "admin", "contrasena": "12341234aA", "tipo_camara": "hikvision" } ] }'
def main(json_parameters):
    data = json.loads(json_parameters)
    print(json.dumps(data, indent=4))

    # Extract necessary data from input
    cam = data["camaras"][0]
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
    
    camara = init_camera(data)
    pan, cross = calcular_angulo_rotacion(cam_coord, ref_coord, emerg_coord, ref_pan)
    print(f"Pan according to rotation in degrees: {pan}")
    if(scale_pan == '01'): pan = scale_angle_0to1(pan, ref_pan, cross)
    if(scale_pan == '-11'): pan = scale_angle_less1to1(pan , ref_pan, cross)
    print(f"Pan for camera movement: {pan}")
    tilt = calculate_camera_tilt(cam_coord, emerg_coord, altura)
    print(f"Tilt before scaling: {tilt}")
    if(scale_tilt == '01'): tilt = scale_angle_90degresstilt(tilt)
    if(scale_tilt == '-11'): tilt = scale_angle_less1to1_90degresstilt(tilt)
    print(f"Tilt for camera movement: {tilt}")
    zoom = calculate_zoom(cam_coord, emerg_coord, zoom_min, zoom_max)
    print(f"Calculated zoom: {zoom}")
    print(f"Moving camera to Pan: {pan}, Tilt: {tilt}, Zoom: {zoom}")
    camara.move(pan,tilt, zoom)

if __name__ == '__main__':
    sys.exit(main(json_parameters))
