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
mixer1_OFF = [1, 5, 0, 0, 0, 0, 137, 202]

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


def send_command_and_confirm(ser, command):
    # Convert command list to bytes
    command_bytes = bytes(command)
    
    # Reset input and output buffer to avoid data corruption
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    
    # Send the command
    ser.write(command_bytes)

    # Wait for the device to process the command and respond
    time.sleep(1)
    
    # Check if there are bytes to read
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        response = ser.read(bytesToRead)
        print("Response received:", response)

        # Example check: if the response is the echo of the command, confirm success
        if response == command_bytes:
            print("Command executed successfully.")
            return True
        else:
            print("Command failed or unexpected response.")
            return False
    else:
        print("No response from device.")
        return False
    
def setMixer1(ser, state):
    if state:
        result = send_command_and_confirm(ser, mixer1_ON)
        print("Mixer 1 ON:", "Success" if result else "Failed")
    else:
        result = send_command_and_confirm(ser, mixer1_OFF)
        print("Mixer 1 OFF:", "Success" if result else "Failed")

def setMixer2(state):
    if state == True:
        ser.write(mixer2_ON)
    else:
        ser.write(mixer2_OFF)        

def setMixer3(state):
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
        




