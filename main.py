from scheduler import *
from cnn_ai import *
from mqttHelper import *
# from cnn_ai import *
import sys
import json
from Adafruit_IO import MQTTClient
import time
import random
import threading
from datetime import datetime
from fsm_auto import *
from physical import *


temp_value = 0
moisture_value = 0


# Predict_lock = threading.Lock()


in_seq1 = array([0, 0, 0, 0, 0, 0, 0, 0, 0])
in_seq2 = array([0, 0, 0, 0, 0, 0, 0, 0, 0])
out_seq = array([in_seq1[i]+in_seq2[i] for i in range(len(in_seq1))])
model = Sequential()
n_steps_in = 0
n_steps_out= 0 
n_features = 0


# Set up timer to update scheduler
def timer_callback(): #set timer to 1 second
    SCH_Update()
    threading.Timer(1.0, timer_callback).start()
threading.Timer(1.0, timer_callback).start()
    
def runCycles(cycle, flow1, flow2, flow3, area, startTime, stopTime):
    global client
    print("Running cycle ...")
    startTime_obj = datetime.strptime(startTime, "%H:%M")
    stopTime_obj = datetime.strptime(stopTime, "%H:%M")
    # print (f'Cycle: {cycle}; Flow1: {flow1}; Flow2: {flow2}; Flow3: {flow3}; Area: {area}; Start time: {startTime}; Stop time: {stopTime}')
    startTime = startTime_obj.hour * 3600 + startTime_obj.minute * 60
    stopTime = stopTime_obj.hour * 3600 + stopTime_obj.minute * 60
    duration = stopTime - startTime
    # print (f'Start time: {startTime}; Stop time: {stopTime}')
    cycle = int(cycle)
    area = int (area)
    while True:
        # current_time = time.localtime().tm_hour * 3600 + time.localtime().tm_min * 60 + time.localtime().tm_sec 
        current_time = time.localtime().tm_hour * 3600 + time.localtime().tm_min * 60 + time.localtime().tm_sec + 3600*6
        # print (f'Current time: {current_time}')
        if current_time >= startTime and current_time <= stopTime and cycle > 0:
            while True:
                status = INIT
                flag = fsm_auto(flow1, flow2, flow3, area, client)
                if flag == 1:
                    break
                time.sleep(1)
            cycle -= 1
            area += 1
            if (area > 3): area = 1
        elif current_time > stopTime or cycle == 0:
            break
        else:
            time.sleep(1)
# MAIN 
def listenSensor():
    global temp_value, moisture_value
    # temp_value = random.randint(20, 40)
    # moisture_value = random.randint(30, 80)
    temp_value = readTemperature()/100
    moisture_value = readMoisture()
    # client.publish("temp", temp_value)
    # client.publish("moist", moisture_value)
    publish_temp(temp_value)
    publish_moist(moisture_value)

def runCommand():
    if is_runCommand_flag():
        print("Running command ...")
        cycleThread = threading.Thread(target=runCycles, args=(get_schedule('cycle'), get_schedule('flow1'), get_schedule('flow2'), get_schedule('flow3'), get_schedule('area'), get_schedule('startTime'), get_schedule('stopTime')))
        cycleThread.start()
        # print ('Start thread successfully')
        set_runCommand_flag(False)

def prepare_model ():
    print ("Preparing model ...")
    global model, in_seq1, in_seq2, out_seq, n_steps_in, n_steps_out, n_features
    model, in_seq1, in_seq2, out_seq, n_steps_in, n_steps_out, n_features = prepare_cnn_model(temp_value, moisture_value)

def predict():
    global model, in_seq1, in_seq2, out_seq, n_steps_in, n_steps_out, n_features 
    predict_temp_1, predict_mois_1,predict_temp_2, predict_mois_2,predict_temp_3, predict_mois_3, model, in_seq1, in_seq2, out_seq, n_steps_in, n_steps_out, n_features = predict_value(temp_value, moisture_value, model, in_seq1, in_seq2, out_seq, n_steps_in, n_steps_out, n_features)
    # client.publish("temp_predict", int(predict_temp_1))
    # client.publish("moist_predict", int (predict_mois_1))
    publish_temp_predict(int(predict_temp_1))
    publish_moist_predict(int (predict_mois_1))
    if predict_temp_1 > 30 and predict_temp_2 > 30 and predict_temp_3 > 30:
        # set_sendPredict_flag(True)
        publish_announceUser(1)
    elif predict_mois_1 > 70 and predict_mois_2 > 70 and predict_mois_3 > 70:
        publish_announceUser(1)
        # set_sendPredict_flag(True)
    elif temp_value > 30 and moisture_value > 70:
        publish_announceUser(1)
        # set_sendPredict_flag(True)

        
SCH_Add_Task(listenSensor, 0, 5)
SCH_Add_Task (prepare_model, 0, 0)
SCH_Add_Task (predict, 1, 5)
SCH_Add_Task (runCommand, 0, 3)
while True:
    SCH_Dispatch_Tasks()