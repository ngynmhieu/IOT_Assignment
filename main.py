from all import *
from scheduler import *
# from cnn_ai import *
import sys
import json
# from Adafruit_IO import MQTTClient
import time
import random
import threading

AIO_FEED_IDs = ["Command"]
AIO_USERNAME = "IOT_232"
AIO_KEY = ""    


temp_value = 0
moisture_value = 0



cycle = None
flow1 = None
flow2 = None
flow3 = None
area = None
schedulerName = None
startTime = None
stopTime = None

sendPredict_flag = False
runCommand_flag = False
Predict_lock = threading.Lock()


in_seq1 = array([0, 0, 0, 0, 0, 0, 0, 0, 0])
in_seq2 = array([0, 0, 0, 0, 0, 0, 0, 0, 0])
out_seq = array([in_seq1[i]+in_seq2[i] for i in range(len(in_seq1))])
model = Sequential()
n_steps_in = 0
n_steps_out= 0 
n_features = 0

# def connected(client):
#     print("Ket noi thanh cong ...")
#     for topic in AIO_FEED_IDs:
#         client.subscribe(topic)

# def subscribe(client , userdata , mid , granted_qos):
#     print("Subscribe thanh cong ...")

# def disconnected(client):
#     print("Ngat ket noi ...")
#     sys.exit (1)

# def message(client , feed_id , payload):
#     print("Nhan du lieu: " + payload + ", feed id: " + feed_id)
#     global cycle, flow1, flow2, flow3, area, schedulerName, startTime, stopTime
#     try:
#         data = json.loads(payload)
#         print(f"Processed JSON data: {data}")
#         cycle = data.get('cycle', cycle)
#         flow1 = data.get('flow1', flow1)
#         flow2 = data.get('flow2', flow2)
#         flow3 = data.get('flow3', flow3)
#         schedulerName = data.get('schedulerName', schedulerName)
#         startTime = data.get('startTime', startTime)
#         stopTime = data.get('stopTime', stopTime)
#         area = data.get('area', area)
#     except json.JSONDecodeError:
#         print("Error decoding JSON")


#Set up Adafruit IO MQTT Client
# client = MQTTClient(AIO_USERNAME , AIO_KEY)
# client.on_connect = connected
# client.on_disconnect = disconnected
# client.on_message = message
# client.on_subscribe = subscribe
# client.connect()
# client.loop_background()

# while True:
#     try:
#         if cycle is not None:
#             client.publish('Command', json.dumps({"cycle": cycle}))
#             client.publish('Command', json.dumps({"flow1": flow1}))
#             client.publish('Command', json.dumps({"flow2": flow2}))
#             client.publish('Command', json.dumps({"flow3": flow3}))
#             client.publish('Command', json.dumps({"area": area}))
#         time.sleep(10)  
#     except Exception as e:
#         print(f"Failed to publish: {str(e)}")
#         time.sleep(5)


# Set up timer to update scheduler
def timer_callback(): #set timer to 1 second
    SCH_Update()
    threading.Timer(1.0, timer_callback).start()
threading.Timer(1.0, timer_callback).start()
    



# temp = 20
# mois = 50


    



# MAIN 
def listenSensor():
    global temp_value, moisture_value
    # temp_value = readTemperature()
    # moisture_value = readMoisture()
    temp_value = random.randint(20, 30)
    moisture_value = random.randint(40, 60)
    # print (f'The value of temp is {temp_value}')
    # print (f'The value of moisture is {moisture_value}')
    return 0
def sendPredict():
    global sendPredict_flag
    if sendPredict_flag:
        print ("Sending predict ...")
        sendPredict_flag = False
    return 0
def runCommand():
    global runCommand_flag
    if runCommand_flag:
        print("Running command ...")
        runCommand_flag = False
    return 0

def prepare_model ():
    print ("Preparing model ...")
    global model, in_seq1, in_seq2, out_seq, n_steps_in, n_steps_out, n_features
    model, in_seq1, in_seq2, out_seq, n_steps_in, n_steps_out, n_features = prepare_cnn_model(temp_value, moisture_value)
    # print (f'nsi: {n_steps_in}, nso: {n_steps_out}, nf: {n_features}')
    # print (f'In_seq1: {in_seq1}')
    # print (f'In_seq2: {in_seq2}')
    return 0

def predict():
    global sendPredict_flag, model, in_seq1, in_seq2, out_seq, n_steps_in, n_steps_out, n_features 
    predict_temp_1, predict_mois_1,predict_temp_2, predict_mois_2,predict_temp_3, predict_mois_3, model, in_seq1, in_seq2, out_seq, n_steps_in, n_steps_out, n_features = predict_value(temp_value, moisture_value, model, in_seq1, in_seq2, out_seq, n_steps_in, n_steps_out, n_features)
    print (f'Predicted temp: {predict_temp_1}, {predict_temp_2}, {predict_temp_3} Predicted mois: {predict_mois_1}, {predict_mois_2}, {predict_mois_3}')
    if predict_temp_1 > 35 and predict_temp_2 >35 and predict_temp_3 >35:
        sendPredict_flag = True
    elif predict_mois_1 > 75 and predict_mois_2 > 75 and predict_mois_3 > 75:
        sendPredict_flag = True
        
        
SCH_Add_Task(listenSensor, 0, 3)
SCH_Add_Task (prepare_model, 0, 0)
SCH_Add_Task (predict, 0, 3)
SCH_Add_Task(sendPredict, 0, 3)
SCH_Add_Task (runCommand, 0, 3)
while True:
    SCH_Dispatch_Tasks()

    # print (f'P redicted temp: {predict_temp_1}, {predict_temp_2}, {predict_temp_3} Predicted mois: {predict_mois_1}, {predict_mois_2}, {predict_mois_3}')