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
type_camera="ezviz"

json_parameters = '{ "emergencia_id": "1", "coordenada": [ 10.364744, -66.977883 ], "camaras": [ { "id": 1, "scale_pan": "01", "scale_tilt": "01", "scale_zoom": "03", "coordenada_camara": [ 10.365072129702737, -66.9775462486802 ], "coordenada_referencia": [ 10.364764751417162, -66.97756636524517 ], "altura": 45, "origen_ptz": [ 0.565, 1, 0 ], "vpn": "wg0", "ip": "10.0.0.4", "puerto": 80, "usuario": "davidvalorwork@gmail.com", "contrasena": "14141313aA@@", "serial": "BB2643869" } ] }'

def main(json_parameters):
    data = json.loads(json_parameters)
    print(json.dumps(data, indent=4))
    # data["coordenada"] = (10.36500155145449, -66.97778161250672) # Bocono
    # data["coordenada"] = (10.365006828332977, -66.97706278051929) # meta
    # data["coordenada"] = (10.365654678419954, -66.97793301987491) # berta
    # data["coordenada"] = (10.366164343123057, -66.97679802169682) # pao
    # data["coordenada"] = (10.364618573568935, -66.97791360268778) # estacionamiento

    # Extract necessary data from input
    cam = data["camaras"][0]
    cam_coord = cam["coordenada_camara"]
    ref_coord = cam["coordenada_referencia"]
    emerg_coord = data["coordenada"]
    ref_pan = cam["origen_ptz"][0]
    altura = cam["altura"]
    scale_pan = cam["scale_pan"]
    scale_tilt = cam["scale_tilt"]
    scale_zoom = cam["scale_zoom"]
    zoom_min = cam["zoom_min"]
    zoom_max = cam["zoom_max"]
    
    camara = init_camera(data, type_camera)
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
