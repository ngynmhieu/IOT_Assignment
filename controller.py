import sys
import json
from Adafruit_IO import MQTTClient
import time
import random
from all import *

AIO_FEED_IDs = ["command", "announceUser", "deviceActive"]
AIO_USERNAME = "IOT_232"
AIO_KEY = ""  

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + ", feed id: " + feed_id)
    global cycle, flow1, flow2, flow3, area, startTime, stopTime, area, runCommand_flag
    if feed_id == 'command':
        try:
            data = json.loads(payload)
            cycle = data['cycle']
            flow1 = data['flow1']
            flow2 = data['flow2']
            flow3 = data['flow3']
            area = data['area']
            startTime = data['startTime']
            stopTime = data['stopTime']
            area = data['area']
            runCommand_flag = True
        except json.JSONDecodeError:
            print("Error decoding JSON")

# Set up Adafruit IO MQTT Client
client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
