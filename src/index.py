from bottle import Bottle, request, response
from main import main
import json

app = Bottle()

@app.route('/receive_json', method='POST')
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
  
@app.route('/move', method='POST')
def move():
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

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)


# curl -X POST http://localhost:8080/receive_json -H "Content-Type: application/json" -d '{"emergencia_id": "1", "coordenada": [ -33.564374585967286, -70.55213001080034 ], "scale_pan": "-11", "scale_tilt": "01", "scale_zoom": "03", "camaras": [ { "id": 1, "coordenada_camara": [ -33.56467351554227, -70.55168811687197 ], "coordenada_referencia": [ -33.56488416249139, -70.55192750401524 ], "altura": 3, "origen_ptz": [ 0.143, 0.5, 0 ], "vpn": "wg0", "ip": "192.168.0.64", "puerto": 80, "usuario": "admin", "contrasena": "12341234aA" } ]}'"
