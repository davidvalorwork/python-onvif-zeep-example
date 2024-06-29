from utils.ezviz.index import Ezviz
from utils.onvif.init import Onvif

def init_camera(camera_data):
  c_data = camera_data['camaras'][0]
  if(c_data['tipo_camara'] == 'ezviz'):
    camera = Ezviz(c_data['usuario'], c_data['contrasena'], c_data['serial'])
  if(c_data['tipo_camara'] == 'hikvision'):
    camera = Onvif(c_data['ip'], c_data['puerto'], c_data['usuario'], c_data['contrasena'])

  return camera