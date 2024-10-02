from utils.camera_kafka import Consumer
import threading
import signal
import sys


def start_consumer_in_background():
    consumer = Consumer("onvif_example")
    consumer.star_read()


def signal_handler(sig, frame):
    print('Shutting down...')
    sys.exit(0)


def start_background_consumer():
    consumer_thread = threading.Thread(target=start_consumer_in_background)
    consumer_thread.daemon = True
    consumer_thread.start()
    signal.signal(signal.SIGINT, signal_handler)
