import time
import serial.tools.list_ports
import queue
import threading
command_queue = queue.Queue()

# Command type flags
READING_SENSORS = 0
CONTROLLING_DEVICE = 1
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



soil_temperature = [1, 3, 0, 6, 0, 1, 100, 11]
soil_moisture = [1, 3, 0, 7, 0, 1, 53, 203]



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

 


def send_command(command, command_type):
    ser.write(command)
    command_queue.put(command_type)
    time.sleep(1)  # Give some time for the device to respond

# Improved function to handle serial responses
def serial_read_response(ser):
    if not command_queue.empty():
        current_command_type = command_queue.get()
        bytesToRead = ser.inWaiting()
        if bytesToRead > 0:
            response = ser.read(bytesToRead)
            response_array = list(response)
            if current_command_type == CONTROLLING_DEVICE:
                return response_array[:6]  # Only relevant part for control commands
            elif current_command_type == READING_SENSORS:
                return response_array  # Full response for sensor readings
        else:
            print("No response received.")
    return []

# Example usage for a device control command
def setMixer1(state):
    command = mixer1_ON if state else mixer1_OFF
    print(f"MIX1 {'ON' if state else 'OFF'}: ")
    send_command(command, CONTROLLING_DEVICE)
    response = serial_read_response(ser)
    expected_response = command[:6]
    if response == expected_response:
        print("Successfully controlled")
    else:
        print("Failed to control")

def setMixer2(state):
    command = mixer2_ON if state else mixer2_OFF
    print(f"MIX2 {'ON' if state else 'OFF'}: ")
    send_command(command, CONTROLLING_DEVICE)
    response = serial_read_response(ser)
    expected_response = command[:6]
    if response == expected_response:
        print("Successfully controlled")
    else:
        print("Failed to control")

def setMixer3(state):
    command = mixer3_ON if state else mixer3_OFF
    print(f"MIX3 {'ON' if state else 'OFF'}: ")
    send_command(command, CONTROLLING_DEVICE)
    response = serial_read_response(ser)
    expected_response = command[:6]
    if response == expected_response:
        print("Successfully controlled")
    else:
        print("Failed to control")

def setSelector1(state):
    command = selector1_ON if state else selector1_OFF
    print(f"Selector1 {'ON' if state else 'OFF'}: ")
    send_command(command, CONTROLLING_DEVICE)
    response = serial_read_response(ser)
    expected_response = command[:6]
    if response == expected_response:
        print("Successfully controlled")
    else:
        print("Failed to control")

def setSelector2(state):
    command = selector2_ON if state else selector2_OFF
    print(f"Selector2 {'ON' if state else 'OFF'}: ")
    send_command(command, CONTROLLING_DEVICE)
    response = serial_read_response(ser)
    expected_response = command[:6]
    if response == expected_response:
        print("Successfully controlled")
    else:
        print("Failed to control")

def setSelector3(state):
    command = selector3_ON if state else selector3_OFF
    print(f"Selector3 {'ON' if state else 'OFF'}: ")
    send_command(command, CONTROLLING_DEVICE)
    response = serial_read_response(ser)
    expected_response = command[:6]
    if response == expected_response:
        print("Successfully controlled")
    else:
        print("Failed to control")

def setPump_in(state):
    command = pumpin_ON if state else pumpin_OFF
    print(f"Pump In {'ON' if state else 'OFF'}: ")
    send_command(command, CONTROLLING_DEVICE)
    response = serial_read_response(ser)
    expected_response = command[:6]
    if response == expected_response:
        print("Successfully controlled")
    else:
        print("Failed to control")

def setPump_out(state):
    command = pumpout_ON if state else pumpout_OFF
    print(f"Pump Out {'ON' if state else 'OFF'}: ")
    send_command(command, CONTROLLING_DEVICE)
    response = serial_read_response(ser)
    expected_response = command[:6]
    if response == expected_response:
        print("Successfully controlled")
    else:
        print("Failed to control")

# Example usage for a sensor read command
def readTemperature():
    send_command(soil_temperature, READING_SENSORS)
    response = serial_read_response(ser)
    if len(response) >= 7:
        value_bytes = response[3:5]
        value = int.from_bytes(value_bytes, byteorder='big')
        return value
    return -1

def readMoisture():
    send_command(soil_moisture, READING_SENSORS)
    response = serial_read_response(ser)
    if len(response) >= 7:
        value_bytes = response[3:5]
        value = int.from_bytes(value_bytes, byteorder='big')
        return value
    return -1


