import sys
import json
from Adafruit_IO import MQTTClient
import time
import random
from all import *
from scheduler import *

AIO_FEED_IDs = ["command", "announceUser", "deviceActive", "moist", "moist_predict", "temp", "temp_predict"]
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
    # print("Nhan du lieu: " + payload + ", feed id: " + feed_id)
    if feed_id == 'command':
        try:
            data = json.loads(payload)
            set_schedule(data['cycle'], data['flow1'], data['flow2'], data['flow3'], data['area'], data['startTime'], data['stopTime'])
            set_runCommand_flag(True)
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

sending_count = 1

# def publish_command (data):
#     print ("Publishing command ...")
#     client.publish("command", json.dumps(data))


def publish_announceUser (data):
    if is_publish_flag():
        set_publish_flag(False)
        print ("Publishing announceUser ...")
        client.publish("announceUser", data)
        time.sleep(1)  # Add a delay
        set_publish_flag(True)

def publish_deviceActive (data):
    if is_publish_flag():
        set_publish_flag(False)
        print ("Publishing deviceActive ...")
        client.publish("deviceActive", data)
        time.sleep(1)  # Add a delay
        set_publish_flag(True)
    
def publish_moist (data):
    if is_publish_flag():
        set_publish_flag(False)
        print ("Publishing moist ...")
        client.publish("moist", data)
        time.sleep(3)  # Add a delay
        set_publish_flag(True)

def publish_moist_predict (data):
    if is_publish_flag():
        set_publish_flag(False)
        print  ("Publishing moist_predict ...")
        client.publish("moist_predict", data)
        time.sleep(3)  # Add a delay
        set_publish_flag(True)
    
def publish_temp (data):
    if is_publish_flag():
        set_publish_flag(False)
        print ("Publishing temp ...")
        client.publish("temp", data)
        time.sleep(3)  # Add a delay
        set_publish_flag(True)
    
def publish_temp_predict (data):
    if is_publish_flag():
        set_publish_flag(False)
        print ("Publishing temp_predict ...")
        client.publish("temp_predict", data)
        time.sleep(3)  # Add a delay
        set_publish_flag(True)
    
# def mqtt_publish (topic, data):
#     global sending_count
#     # if (topic == "command"):
#     #     SCH_Add_Task(publish_command(data), sending_count, 0)
#     if (topic == "announceUser"):
#         SCH_Add_Task(publish_announceUser(data), sending_count, 0)
#     elif (topic == "deviceActive"):
#         SCH_Add_Task(publish_deviceActive(data), sending_count, 0)
#     elif (topic == "moist"):
#         SCH_Add_Task(publish_moist(data), sending_count, 0)
#     elif (topic == "moist_predict"):
#         SCH_Add_Task(publish_moist_predict(data), sending_count, 0)
#     elif (topic == "temp"):
#         SCH_Add_Task(publish_temp(data), sending_count, 0)
#     elif (topic == "temp_predict"):
#         SCH_Add_Task(publish_temp_predict(data), sending_count, 0)
#     sending_count += 1
#     time.sleep(1)
#     if (sending_count > 1):
#         sending_count -= 1    
    