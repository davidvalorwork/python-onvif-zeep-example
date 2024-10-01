from kafka import KafkaProducer
import json
import time

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

def get_data():
    return {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

if __name__ == "__main__":
    producer = KafkaProducer(
        bootstrap_servers=["localhost:9092"],
        value_serializer=json_serializer
    )

    while True:
        data = get_data()
        producer.send("onvif_example", data)
        print(f"Sent: {data}")
        time.sleep(5) 