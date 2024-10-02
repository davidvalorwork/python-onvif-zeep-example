# consumer.py
from kafka import KafkaConsumer
from main import main
import json


class Consumer:
    def __init__(self, topic, server='localhost:9092'):
        self._consumer = KafkaConsumer(topic,
                                       bootstrap_servers=''+server,
                                       value_deserializer=lambda x: json.loads(
                                           x.decode('utf-8')),
                                       group_id='onvif-example-group')

        self.data = []

    @property
    def consumer(self):
        return self._consumer

    @consumer.setter
    def consumer(self, value):
        if isinstance(value, KafkaConsumer):
            self._consumer = value

    def star_read(self):
        self.receive_message()

    def receive_message(self):
        message_count = 0
        for message in self._consumer:
            message = message.value
            print(f'Message {message_count}: {message}')
            self.data.append(message)
            message_count += 1
            try:
                main(json.dumps(message))
            except Exception as e:
                print(e)


if __name__ == '__main__':
    # consumer = Consumer("onvif_example")
    # consumer.star_read()
    pass
