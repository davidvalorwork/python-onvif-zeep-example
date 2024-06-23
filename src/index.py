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

if __name__ == '__main__':
  app.run(host='localhost', port=8080, debug=True)