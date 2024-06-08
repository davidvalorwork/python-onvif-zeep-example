from onvif import ONVIFCamera

def init_onvif():
    # Crear un objeto cliente ONVIF
    device = ONVIFCamera(
        "192.168.1.145",
        "80",
        "admin",
        "67457172aA@@",
        ".\python-onvif-zeep\wsdl",
        # transport=Transport(timeout=self.timeout),
    )

    service = device.create_ptz_service()
    absolute_move_request = service.create_type("AbsoluteMove")
    pose_dict = {"PanTilt": {"x": 0.0, "y": 0.0}, "Zoom": {"x": 0.0}}
    absolute_move_request.Position = pose_dict
    absolute_move_request.Position["PanTilt"]["x"] = 0
    absolute_move_request.Position["PanTilt"]["y"] = 0
    absolute_move_request.Position["Zoom"]["x"] = 0
    device.AbsoluteMove(absolute_move_request)
