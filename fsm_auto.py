from all import *
from physical import *



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
        client.publish("deviceActive", 0)
        start_time = time.time()
        # print ("INIT")
        status = MIX1
        client.publish("deviceActive", 1)
        
        
    elif (status == MIX1):
        #DO SOMETHING
        setDevice1(1)
        end_time = time.time()
        # print ("MIX1")
        if (end_time - start_time >= 5):
            start_time = time.time()
            status = MIX2
            setDevice1(0)
            client.publish("deviceActive", 2)
            
    elif (status == MIX2):
        #DO SOMETHING
        # print ("MIX2")
        setDevice2(1)
        end_time = time.time()
        if (end_time - start_time >= 5):
            start_time = time.time()
            status = MIX3
            setDevice2(0)
            client.publish("deviceActive", 3)
            
    elif (status == MIX3):
        # print ('MIX3')
        #DO SOMETHING
        setDevice3(1)
        end_time = time.time()
        if (end_time - start_time >= 5):
            start_time = time.time()
            setDevice3(0)
            status = PUMP_IN
            client.publish("deviceActive", 4)
              
    elif (status == PUMP_IN):
        #DO SOMETHING
        # print ('PUMP_IN')
        setDevice7(1)
        end_time = time.time()
        if (end_time - start_time >= 5):
            start_time = time.time()
            setDevice7(0)
            status = SELECTOR
            if area == 1:
                setDevice4(1)
            elif area == 2:
                setDevice5(1)
            elif area == 3:
                setDevice4(1)
                
    elif (status == SELECTOR):
        # print ('SELECTOR')
        start_time = time.time()
        status = PUMP_OUT
        if area == 1:
            setDevice4(0)
        elif area == 2:
            setDevice5(0)
        elif area == 3:
            setDevice6(0)
        client.publish("deviceActive", 8)
        
    elif (status == PUMP_OUT):
        # print ('PUMP_OUT')
        setDevice8(1)
        start_time = time.time()
        setDevice8(0)
        status = NEXT_CYCLE
        client.publish("deviceActive", 9)
        
    elif (status == NEXT_CYCLE):
        status = INIT
        
        return 1
    else:
        print("Error: Unknown state")
        start_time = time.time()
        status = INIT



