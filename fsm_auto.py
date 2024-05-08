<<<<<<< HEAD
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
=======
import time
from physical import *

# Define FSM states
INIT, MIXER1, MIXER2, MIXER3, PUMPIN, SELECTOR, PUMPOUT, NEXTCYCLE = range(8)

state = INIT
running = True
while running:
    if state == INIT:
        if receive_schedule():
            state = MIXER1
        else:
            running = False
    elif state == MIXER1:
        mixer_1()
        state = MIXER2
    elif state == MIXER2:
        mixer_2()
        state = MIXER3
    elif state == MIXER3:
        mixer_3()
        state = PUMPIN
    elif state == PUMPIN:
        pump_in()
        state = SELECTOR
    elif state == SELECTOR:
        selector()
        state = PUMPOUT
    elif state == PUMPOUT:
        pump_out()
        if enough_fertilizer_and_water():
            state = NEXTCYCLE
        else:
            running = False
    elif state == NEXTCYCLE:
        next_cycle()
        state = INIT
    time.sleep(1)
>>>>>>> 2105badb2c78aa943b5a6ef58560816e5a7001e6
