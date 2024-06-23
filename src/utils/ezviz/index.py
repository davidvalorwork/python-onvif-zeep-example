from pyezviz import EzvizClient, EzvizCamera
from utils.ezviz.movements import move_coordinates

class Ezviz:
    def __init__(self, usuario, contrasena, serial):
      self.init_logs(usuario, contrasena, serial)
      self.client = EzvizClient(usuario, contrasena, "sa")
      self.client.login()
      self.camera = EzvizCamera(self.client, serial)
      self.init_end_logs()
    
    def move(self, x, y, z=0):
        try:
          move_coordinates(self.camera, x, y)
        except Exception as e:
            print("ERROR MOVING CAMERA")
            print("--------------------")
            print(e)














    
    def init_logs(self, usuario, contrasena, serial):
      print("Iniciando camara ezviz...")
      print("Usuario " + usuario)
      print("Contrasena " + contrasena)
      print("Serial " + serial)
      print("--------------------")

    def init_end_logs(self):
      print("Camara ezviz iniciada...")
      print("--------------------")