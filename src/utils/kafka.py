from confluent_kafka import consumer

servers = 'host:9092'

conf = {
    'bootstrap.servers': servers,
    'group.id': 'foo',
    'auto.offset.reset': 'smallest'
}

consumer = Consumer(conf)
