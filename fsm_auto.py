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
        publish_deviceActive(0)
        start_time = time.time()
        #print ("INIT")
        status = MIX1
        #print ("MIX1")
        setMixer1(True)
        publish_deviceActive(1)
        
        
    elif (status == MIX1):
        #DO SOMETHING
        end_time = time.time()
        if (end_time - start_time >= 5):
            start_time = time.time()
            status = MIX2
            #print ("MIX2")
            setMixer1(False)
            setMixer2(True)
            publish_deviceActive(2)
            
    elif (status == MIX2):
        #DO SOMETHING
        end_time = time.time()
        if (end_time - start_time >= 5):
            start_time = time.time()
            status = MIX3
            #print ("MIX3")
            setMixer2(False)
            setMixer3(True)
            publish_deviceActive(3)
            
    elif (status == MIX3):
        #DO SOMETHING
        end_time = time.time()
        if (end_time - start_time >= 5):
            start_time = time.time()
            #print ("PUMP_IN")
            setMixer3(False)
            setPump_in(True)
            status = PUMP_IN
            publish_deviceActive(4)
              
    elif (status == PUMP_IN):
        #DO SOMETHING
        end_time = time.time()
        if (end_time - start_time >= 5):
            start_time = time.time()
            setPump_in(False)
            status = SELECTOR
            if area == 1:
                #print ('SELECTOR1')
                setSelector1(True)
                publish_deviceActive(5)
            elif area == 2:
                #print ('SELECTOR2')
                setSelector2(True)
                publish_deviceActive(6)
            elif area == 3:
                #print ('SELECTOR3')
                setSelector3(True)
                publish_deviceActive(7)
    elif (status == SELECTOR):
        # print ('SELECTOR')
        start_time = time.time()
        status = PUMP_OUT
        #print ('PUMP_OUT')
        setPump_out(True)
        setSelector1(False)
        setSelector2(False)
        setSelector3(False)
        publish_deviceActive(8)
        
    elif (status == PUMP_OUT):
        # print ('PUMP_OUT')
        start_time = time.time()
        #print ('NEXT_CYCLE')
        setPump_out(False)
        status = NEXT_CYCLE
        publish_deviceActive(9)
        
    elif (status == NEXT_CYCLE):
        #print ('INIT')
        status = INIT
        publish_deviceActive(0)
        return 1
    else:
        print("Error: Unknown state")
        start_time = time.time()
        status = INIT



