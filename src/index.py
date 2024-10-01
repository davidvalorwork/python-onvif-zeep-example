from bottle import Bottle, request, response, view
from main import main
import json
from utils.init_camera import init_camera

app = Bottle()
route = app.route

@route('/receive_json', method='POST')
def receive_json():
  try:
    data = request.json
    if data is None:
      raise ValueError("No JSON payload received.")
    # Process the JSON data as needed
    print("Received JSON:", data)
    main(json.dumps(data))
    return {"status": "success", "message": "JSON received successfully."}
  except ValueError as e:
    response.status = 400
    return {"status": "error", "message": str(e)}
  
@route('/move', method='POST')
def move():
  ptz = request.json
  if not ptz:
    return {"status": "error", "message": "PTZ parameter is missing."}
  try:
    ptz_data = ptz
    pan = float(ptz_data.get('pan'))
    tilt = float(ptz_data.get('tilt'))
    zoom = float(ptz_data.get('zoom'))
    camaras = ptz_data.get('camaras')

    print(f"Received PTZ: Pan: {pan}, Tilt: {tilt}, Zoom: {zoom}, Camera data: {camaras}")

    if None in (pan, tilt, zoom, camaras):
      return {"status": "error", "message": "Missing pan, tilt, zoom, or camera data."}
  
    camara = init_camera(ptz_data)

    camara.move(pan, tilt, zoom)

    return {"status": "success", "message": "Camera moved successfully."}
  except ValueError as e:
    print(e)
    return {"status": "error", "message": "Invalid PTZ format. Ensure it is a valid JSON."}
  except Exception as e:
    print(e)
    return {"status": "error", "message": str(e)}
  
@route('/', method='GET')
@view('index.html')
def index():
  return dict()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)

