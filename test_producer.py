from kafka import KafkaProducer
import json
import time


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


def get_data():
    return {
        "emergencia_id": "1",
        "coordenada": [10.364744,
                       -66.977883],
        "camaras": [
            {
                "id": 1,
                "scale_pan": "01",
                "scale_tilt": "01",
                "scale_zoom": "03",
                "coordenada_camara": [10.365072129702737,
                                      -66.9775462486802],
                "coordenada_referencia": [10.364764751417162,
                                          -66.97756636524517],
                "altura": 45,
                "origen_ptz": [0.565,
                               1,
                               0],
                "vpn": "wg0",
                "ip": "10.0.0.4",
                "puerto": 80,
                "usuario": "davidvalorwork@gmail.com",
                "contrasena": "14141313aA@@",
                "serial": "BB2643869",
                "zoom_min": 0,
                "zoom_max": 1,
                "min_tilt_optimization_distance": 10,
                "tilt_optimization": 2,
                "tipo_camara": "ezviz"
            }]}


if __name__ == "__main__":
    producer = KafkaProducer(
        bootstrap_servers=["localhost:9092"],
        value_serializer=json_serializer
    )

    while True:
        data = get_data()
        producer.send("onvif_example",
                      data)
        print(f"Sent: {data}")
        time.sleep(30)
