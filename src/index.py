import sys
import json
from utils.init_camera import init_camera

usuario="davidvalorwork@gmail.com"
password= "14141313aA@@"
serial = "BB2643869"
type_camera="ezviz"

json_parameters = '{"emergencia_id":"1","coordenada":[10.364744,-66.977883],"camaras":[{"id":1,"coordenada_camara":[10.365224,-66.977692],"coordenada_referencia":[10.364621,-66.977600],"altura":45,"origen_ptz":[0.5,1,0],"vpn":"wg0","ip":"10.0.0.4","puerto":80,"usuario":"davidvalorwork@gmail.com","contrasena":"14141313aA@@", "serial":"BB2643869"}]}'

def main(json_parameters):
    data = json.loads(json_parameters)
    print(json.dumps(data, indent=4))
    camara = init_camera(data, type_camera)
    print(camara)
    camara.move(0.565,0.5)
    camara.move(0.012228428223553633,0.5)
    camara.move(0.565,0.5)

if __name__ == '__main__':
    sys.exit(main(json_parameters))
