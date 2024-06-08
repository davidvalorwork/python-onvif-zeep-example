from utils.ezviz.index import Ezviz

def init_camera(camera_data, type_camera):
  c_data = camera_data['camaras'][0]
  if(type_camera == 'ezviz'):
    camera = Ezviz(c_data['usuario'], c_data['contrasena'], c_data['serial'])

  return camera