from onvif import ONVIFCamera
from pyezviz import EzvizClient, EzvizCamera
import platform
import sys
from photo import take_photo

def get_python_version():
    python_version = platform.python_version().split(".")
    python_version = python_version[0] + "." + python_version[1]
    return python_version

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

def movements(camera, direction, step, number):
    # Only 8 movements to up and to down
    for x in range(number):
        camera.move(direction,step)

def move_coordinates(camera, x, y):
    print("Moving to " + str(x) + ' ' + str(y))
    camera.move_coordinates(x,y)
    movements(camera, 'down', 1, int(10-(y*10)))

def move_origin(camera):
    camera.move_coordinates(0.6, 1)
    movements(camera, 'up', 1, 8)

def init_ezviz():
    client = EzvizClient("davidvalorwork@gmail.com", "67457172aA@@", "sa")
    try:
        client.login()
        camera = EzvizCamera(client, "BB2643869")
        move_origin(camera)
        take_photo('sky')
        move_coordinates(camera,0.8,0.2)
        take_photo('vecinos_15-A')
        move_coordinates(camera,0.8,0)
        take_photo('vecinos')
        move_origin(camera)
        print("Camera loaded")
    except Exception as e:
        print(e)
        return 1
    finally:
        client.close_session()


if __name__ == '__main__':
    while True:
        try:
            init_ezviz()
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    sys.exit()
