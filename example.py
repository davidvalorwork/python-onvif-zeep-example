from onvif import ONVIFCamera
import platform


def get_python_version():
    python_version = platform.python_version().split(".")
    python_version = python_version[0] + "." + python_version[1]
    return python_version


# Crear un objeto cliente ONVIF
device = ONVIFCamera(
    "192.168.1.10",
    "8080",
    "admin",
    "password",
    "/app/python-onvif-zeep/wsdl",
    # transport=Transport(timeout=self.timeout),
)


# Descubrir dispositivos ONVIF
devices = device.discovery.probe()

# Imprimir la información de los dispositivos descubiertos
for device in devices:
    print(device.XAddr)
    print(device.ServiceURL)

service = device.create_ptz_service()
absolute_move_request = service.create_type("AbsoluteMove")
pose_dict = {"PanTilt": {"x": 0.0, "y": 0.0}, "Zoom": {"x": 0.0}}
absolute_move_request.Position = pose_dict
absolute_move_request.Position["PanTilt"]["x"] = 0
absolute_move_request.Position["PanTilt"]["y"] = 0
absolute_move_request.Position["Zoom"]["x"] = 0
device.AbsoluteMove(absolute_move_request)
