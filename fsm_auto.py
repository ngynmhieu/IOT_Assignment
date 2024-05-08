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
