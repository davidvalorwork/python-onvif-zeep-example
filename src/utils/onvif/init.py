from onvif import ONVIFCamera
import os

class Onvif:
    def __init__(self, ip: str, port: int, usuario: str, contrasena: str):
      print("Iniciando onvif")
      
      wsdl_path = ".\\python-onvif-zeep\\wsdl" if os.name == 'nt' else "./python-onvif-zeep/wsdl"
      
      self.device = ONVIFCamera(ip, port, usuario, contrasena, wsdl_path)
      
      self.ptz_service = self.device.create_ptz_service()
      
      media_service = self.device.create_media_service()
      self.media_profile = media_service.GetProfiles()[0]
      
      print("Conectado a la camara")

    def move(self, x, y, zoom=0.0):
      print(f"Moviendo to coordinates (x={x}, y={y}, zoom={zoom})")
      
      absolute_move_request = self.service.create_type("AbsoluteMove")
      pose_dict = {"PanTilt": {"x": x, "y": y}, "Zoom": {"x": zoom}}
      
      absolute_move_request.Position = pose_dict
      absolute_move_request.ProfileToken = self.media_profile.token
      
      self.ptz_service.AbsoluteMove(absolute_move_request)
      
      print(f"Movido to coordinates (x={x}, y={y}, zoom={zoom})")
