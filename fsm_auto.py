from all import *


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
        end_time = time.time()
        # print ("MIX1")
        if (end_time - start_time >= 5):
            start_time = time.time()
            status = MIX2
            client.publish("deviceActive", 2)
            
    elif (status == MIX2):
        #DO SOMETHING
        # print ("MIX2")
        end_time = time.time()
        if (end_time - start_time >= 5):
            start_time = time.time()
            status = MIX3
            client.publish("deviceActive", 3)
            
    elif (status == MIX3):
        # print ('MIX3')
        #DO SOMETHING
        end_time = time.time()
        if (end_time - start_time >= 5):
            start_time = time.time()
            status = PUMP_IN
            client.publish("deviceActive", 4)
              
    elif (status == PUMP_IN):
        #DO SOMETHING
        # print ('PUMP_IN')
        end_time = time.time()
        if (end_time - start_time >= 5):
            start_time = time.time()
            status = SELECTOR
            if area == 1:
                client.publish("deviceActive", 5)
            elif area == 2:
                client.publish("deviceActive", 6)
            elif area == 3:
                client.publish("deviceActive", 7)
    elif (status == SELECTOR):
        # print ('SELECTOR')
        start_time = time.time()
        status = PUMP_OUT
        client.publish("deviceActive", 8)
        
    elif (status == PUMP_OUT):
        # print ('PUMP_OUT')
        start_time = time.time()
        status = NEXT_CYCLE
        client.publish("deviceActive", 9)
        
    elif (status == NEXT_CYCLE):
        status = INIT
        
        return 1
    else:
        print("Error: Unknown state")
        start_time = time.time()
        status = INIT
