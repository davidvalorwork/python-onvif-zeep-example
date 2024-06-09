from onvif import ONVIFCamera

class Onvif:
    def __init__(self, ip, port, usuario, contrasena):
      print("Iniciando onvif")
      self.device = ONVIFCamera(
        ip,
        port,
        usuario,
        contrasena,
        ".\python-onvif-zeep\wsdl",
        # transport=Transport(timeout=self.timeout),
      )
      self.service = self.device.create_ptz_service()
      self.ptz_service = self.device.create_ptz_service()
      media_service = self.device.create_media_service()
      self.media_profile = media_service.GetProfiles()[0]
      print("Conectado a la camara")

    def move(self,x, y):
        print("Moviendo", x, y)
        absolute_move_request = self.service.create_type("AbsoluteMove")
        pose_dict = {"PanTilt": {"x": x, "y": y}, "Zoom": {"x": 0.0}}
        absolute_move_request.Position = pose_dict
        absolute_move_request.Position["PanTilt"]["x"] = x
        absolute_move_request.Position["PanTilt"]["y"] = y
        absolute_move_request.Position["Zoom"]["x"] = 0
        absolute_move_request.ProfileToken = self.media_profile.token
        self.ptz_service.AbsoluteMove(absolute_move_request)
        print("Movido a", x, y)
