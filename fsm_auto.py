from all import *


status = INIT
start_time = 0
end_time = 0

def fsm_auto():
    if (status == INIT):
        start_time = time.time()
        status = MIX1
        
        
    elif (status == MIX1):
        #DO SOMETHING
        end_time = time.time()
        if (end_time - start_time >= 10):
            start_time = time.time()
            status = MIX2
            
            
    elif (status == MIX2):
        #DO SOMETHING
        end_time = time.time()
        if (end_time - start_time >= 10):
            start_time = time.time()
            status = MIX3
            
            
    elif (status == MIX3):
        #DO SOMETHING
        end_time = time.time()
        if (end_time - start_time >= 10):
            start_time = time.time()
            status = PUMP_IN
            
            
    elif (status == PUMP_IN):
        #DO SOMETHING
        end_time = time.time()
        if (end_time - start_time >= 20):
            start_time = time.time()
            status = SELECTOR
            
            
    elif (status == SELECTOR):
        start_time = time.time()
        status = PUMP_OUT
        
        
    elif (status == PUMP_OUT):
        start_time = time.time()
        status = INIT
        
        
    else:
        print("Error: Unknown state")
        start_time = time.time()
        status = INIT