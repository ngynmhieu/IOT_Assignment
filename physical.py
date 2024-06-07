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

# def compute_crc(data):
#     crc = 0xFFFF
#     for byte in data:
#         crc ^= byte
#         for _ in range(8):
#             lsb = crc & 1
#             crc >>= 1
#             if lsb:
#                 crc ^= 0xA001
#     return crc

# def correct_crc(array):
#     data = array[:-2]
#     high, low = array[-2:]

#     crc = compute_crc(data)
#     crc_low = (crc >> 8) & 0xFF
#     crc_high = crc & 0xFF
    

#     if (crc_high == high and 
#         crc_low == low):
#         return array
#     else:

#         array_chuan = array[:-2] + [crc_high, crc_low]
#         return array_chuan
     
def serial_read_data(ser):
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        out = ser.read(bytesToRead)
        data_array = list(out)
        print("Data array:", data_array)
        if len(data_array) >= 7:
            value_bytes = data_array[-4:-2]  
            value = int.from_bytes(value_bytes, byteorder='big')  # Change 'big' to 'little' if needed
            return value
        else:
            return -1
    return 0

soil_temperature = [1, 3, 0, 6, 0, 1, 100, 11]
def readTemperature():
    print (f"First read temperature")
    # serial_read_data(ser)
    ser.write(soil_temperature)
    print (f'After write')
    time.sleep(1)
    return serial_read_data(ser)

soil_moisture = [1, 3, 0, 7, 0, 1, 53, 203]
def readMoisture():
    print (f'First read moisture')
    # serial_read_data(ser)
    ser.write(soil_moisture)
    print (f'After write')
    time.sleep(1)
    return serial_read_data(ser)
#test

mixer1_ON  = [1, 5, 0, 0, 255, 0, 140, 58]
mixer1_OFF = [1, 5, 0, 0, 0, 0, 205, 202]

mixer2_ON  = [2, 5, 0, 0, 255, 0, 221, 250]
mixer2_OFF = [2, 5, 0, 0, 0, 0, 156, 10]

mixer3_ON  = [3, 5, 0, 0, 255, 0, 45, 250]
mixer3_OFF = [3, 5, 0, 0, 0, 0, 124, 10]

selector1_ON  = [4, 5, 0, 0, 255, 0, 108, 15]
selector1_OFF = [4, 5, 0, 0, 0, 0, 61, 207]

selector2_ON  = [5, 5, 0, 0, 255, 0, 61, 207]
selector2_OFF = [5, 5, 0, 0, 0, 0, 108, 15]

selector3_ON  = [6, 5, 0, 0, 255, 0, 13, 223]
selector3_OFF = [6, 5, 0, 0, 0, 0, 134, 103]

pumpin_ON  = [7, 5, 0, 0, 255, 0, 180, 7]
pumpin_OFF = [7, 5, 0, 0, 0, 0, 81, 195]

pumpout_ON  = [8, 5, 0, 0, 255, 0, 149, 159]
pumpout_OFF = [8, 5, 0, 0, 0, 0, 240, 47]

#Hieu
def setDevice1(state):
    if state == True:
        ser.write(mixer1_ON)
    else:
        ser.write(mixer1_OFF)

def setDevice2(state):
    if state == True:
        ser.write(mixer2_ON)
    else:
        ser.write(mixer2_OFF)        

def setDevice3(state):
    if state == True:
        ser.write(mixer3_ON)
    else:
        ser.write(mixer3_OFF)

def setDevice4(state):
    if state == True:
        ser.write(selector1_ON)
    else:
        ser.write(selector1_OFF)

def setDevice5(state):
    if state == True:
        ser.write(selector2_ON)
    else:
        ser.write(selector2_OFF)

def setDevice6(state):
    if state == True:
        ser.write(selector3_ON)
    else:
        ser.write(selector3_OFF)

def setDevice7(state):
    if state == True:
        ser.write(pumpin_ON)
    else:
        ser.write(pumpin_OFF)

def setDevice8(state):
    if state == True:
        ser.write(pumpout_ON)
    else:
        ser.write(pumpout_OFF)
        




