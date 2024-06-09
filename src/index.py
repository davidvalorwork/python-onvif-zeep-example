import sys
import json
from utils.init_camera import init_camera

usuario="davidvalorwork@gmail.com"
password= "14141313aA@@"
serial = "BB2643869"
type_camera="ezviz"

json_parameters = '{"emergencia_id":"1","coordenada":[10.364744,-66.977883],"camaras":[{"id":1,"coordenada_camara":[10.365072129702737,-66.9775462486802],"coordenada_referencia":[10.364764751417162,-66.97756636524517],"altura":45,"origen_ptz":[0.565,1,0],"vpn":"wg0","ip":"10.0.0.4","puerto":80,"usuario":"davidvalorwork@gmail.com","contrasena":"14141313aA@@", "serial":"BB2643869"}]}'

def main(json_parameters):
    data = json.loads(json_parameters)
    data["coordenada"] = (10.36500155145449, -66.97778161250672) # Bocono
    # data["coordenada"] = (10.365006828332977, -66.97706278051929) # meta
    # data["coordenada"] = (10.365654678419954, -66.97793301987491) # berta
    # data["coordenada"] = (10.366164343123057, -66.97679802169682) # pao
    print(json.dumps(data, indent=4))
    camara = init_camera(data, type_camera)
    print(camara)
    camara.move(0.565,0.5)
    camara.move(0.012228428223553633,0.5)
    camara.move(0.565,0.5)

if __name__ == '__main__':
    sys.exit(main(json_parameters))
