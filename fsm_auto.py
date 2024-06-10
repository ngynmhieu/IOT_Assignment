from all import *
from physical import *
from mqttHelper import *


INIT = 0
MIX1 = 1
MIX2 = 2
MIX3 = 3
PUMP_IN = 4
SELECTOR = 5
PUMP_OUT = 6
NEXT_CYCLE = 7


status = INIT
start_time = 0
end_time = 0

def fsm_auto(flow1, flow2, flow3, area, client):
    global status, start_time, end_time
    if (status == INIT):
        # client.publish("deviceActive", 0)
        publish_deviceActive(0)
        start_time = time.time()
        print ("INIT")
        status = MIX1
        # client.publish("deviceActive", 1)
        print ("MIX1")
        setMixer1(1)
        publish_deviceActive( 1)
        
        
    elif (status == MIX1):
        #DO SOMETHING
        end_time = time.time()
        if (end_time - start_time >= 5):
            start_time = time.time()
            status = MIX2
            # client.publish("deviceActive", 2)
            print ("MIX2")
            setMixer1(0)
            setMixer2(1)
            publish_deviceActive(2)
            
    elif (status == MIX2):
        #DO SOMETHING
        end_time = time.time()
        if (end_time - start_time >= 5):
            start_time = time.time()
            status = MIX3
            print ("MIX3")
            setMixer2(0)
            setMixer3(1)
            # client.publish("deviceActive", 3)
            publish_deviceActive(3)
            
    elif (status == MIX3):
        #DO SOMETHING
        end_time = time.time()
        if (end_time - start_time >= 5):
            start_time = time.time()
            print ("PUMP_IN")
            setMixer3(0)
            setPump_in(1)
            status = PUMP_IN
            # client.publish("deviceActive", 4)
            publish_deviceActive( 4)
              
    elif (status == PUMP_IN):
        #DO SOMETHING
        end_time = time.time()
        if (end_time - start_time >= 5):
            start_time = time.time()
            setPump_in(0)
            status = SELECTOR
            if area == 1:
                print ('SELECTOR1')
                setSelector1(1)
                publish_deviceActive(5)
            elif area == 2:
                print ('SELECTOR2')
                setSelector2(1)
                publish_deviceActive(6)
            elif area == 3:
                print ('SELECTOR3')
                setSelector3(1)
                publish_deviceActive( 7)
    elif (status == SELECTOR):
        # print ('SELECTOR')
        start_time = time.time()
        status = PUMP_OUT
        print ('PUMP_OUT')
        setPump_out(1)
        setSelector1(0)
        setSelector2(0)
        setSelector3(0)
        publish_deviceActive(8)
        
    elif (status == PUMP_OUT):
        # print ('PUMP_OUT')
        start_time = time.time()
        print ('NEXT_CYCLE')
        setPump_out(0)
        status = NEXT_CYCLE
        publish_deviceActive( 9)
        
    elif (status == NEXT_CYCLE):
        print ('INIT')
        status = INIT
        publish_deviceActive(0)
        return 1
    else:
        print("Error: Unknown state")
        start_time = time.time()
        status = INIT



