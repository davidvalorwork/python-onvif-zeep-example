from onvif import ONVIFCamera

class init_onvif:
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
      print("Conectado a la camara")

    def move(self,x, y):
        print("Moviendo", x, y)
        absolute_move_request = self.service.create_type("AbsoluteMove")
        pose_dict = {"PanTilt": {"x": x, "y": y}, "Zoom": {"x": 0.0}}
        absolute_move_request.Position = pose_dict
        absolute_move_request.Position["PanTilt"]["x"] = x
        absolute_move_request.Position["PanTilt"]["y"] = y
        absolute_move_request.Position["Zoom"]["x"] = 0
        self.device.AbsoluteMove(absolute_move_request)
        print("Movido a", x, y)
