import time
import serial.tools.list_ports
def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return commPort
    # return "/dev/ttyUSB1"

portName = getPort()
print(portName)
if portName != "None":
    ser = serial.Serial(port=portName, baudrate=9600)

def serial_read_data(ser):
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        out = ser.read(bytesToRead)
        data_array = list(out)
        if len(data_array) >= 7:
            value_bytes = data_array[3:5]  
            value = int.from_bytes(value_bytes, byteorder='big') 
            return value
        else:
            return -1  
    return 0  

soil_temperature = [1, 3, 0, 6, 0, 1, 100, 11]
def readTemperature():
    ser.write(soil_temperature)
    time.sleep(1)
    return serial_read_data(ser)

soil_moisture = [1, 3, 0, 7, 0, 1, 53, 203]
def readMoisture():
    ser.write(soil_moisture)
    time.sleep(1)
    return serial_read_data(ser)
#test

mixer1_ON  = [1, 6, 0, 0, 0, 255, 201, 138]
mixer1_OFF = [1, 6, 0, 0, 0, 0, 137, 202]

mixer2_ON = [2, 6, 0, 0, 0, 255, 201, 185]
mixer2_OFF = [2, 6, 0, 0, 0, 0, 137, 249]

mixer3_ON  = [3, 6, 0, 0, 0, 255, 200, 104]
mixer3_OFF = [3, 6, 0, 0, 0, 0, 136, 40]

selector1_ON  = [4, 6, 0, 0, 0, 255, 201, 223]
selector1_OFF = [4, 6, 0, 0, 0, 0, 137, 159]

selector2_ON  = [5, 6, 0, 0, 0, 255, 200, 14]
selector2_OFF = [5, 6, 0, 0, 0, 0, 136, 78]

selector3_ON  = [6, 6, 0, 0, 0, 255, 200, 61]
selector3_OFF = [6, 6, 0, 0, 0, 0, 136, 125]

pumpin_ON  = [7, 6, 0, 0, 0, 255, 201, 236]
pumpin_OFF = [7, 6, 0, 0, 0, 0, 137, 172]

pumpout_ON  = [8, 6, 0, 0, 0, 255, 201, 19]
pumpout_OFF = [8, 6, 0, 0, 0, 0, 137, 83]

 
def setMixer1(state):
    if state == True:
        ser.write(mixer1_ON)
    else:
        ser.write(mixer1_OFF)

def setMixer2(ser, state):
    if state == True:
        ser.write(mixer2_ON)
    else:
        ser.write(mixer2_OFF)    

def setMixer3(ser, state):
    if state == True:
        ser.write(mixer3_ON)
    else:
        ser.write(mixer3_OFF) 

def setSelector1(state):
    if state == True:
        ser.write(selector1_ON)
    else:
        ser.write(selector1_OFF)

def setSelector2(state):
    if state == True:
        ser.write(selector2_ON)
    else:
        ser.write(selector2_OFF)

def setSelector3(state):
    if state == True:
        ser.write(selector3_ON)
    else:
        ser.write(selector3_OFF)

def setPump_in(state):
    if state == True:
        ser.write(pumpin_ON)
    else:
        ser.write(pumpin_OFF)

def setPump_out(state):
    if state == True:
        ser.write(pumpout_ON)
    else:
        ser.write(pumpout_OFF)
        




