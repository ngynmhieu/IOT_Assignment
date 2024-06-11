
#Define the state of the cycle


#import cac file khac


cycle = None
flow1 = None
flow2 = None
flow3 = None
area = None
startTime = None
stopTime = None


publish_flag = False
runCommand_flag = True

def set_publish_flag (value):
    # print ("Set sendPredict_flag to ", value)
    global publish_flag 
    publish_flag = value
    
def set_runCommand_flag (value):
    # print ("Set runCommand_flag to ", value)
    global runCommand_flag
    runCommand_flag = value
    
def set_schedule(cycle_t, flow1_t, flow2_t, flow3_t, area_t, startTime_t, stopTime_t):
    # print ("Set schedule ...")
    global cycle, flow1, flow2, flow3, area, startTime, stopTime
    cycle = cycle_t
    flow1 = flow1_t
    flow2 = flow2_t
    flow3 = flow3_t
    area = area_t
    startTime = startTime_t
    stopTime = stopTime_t

def is_publish_flag():
    return publish_flag

def is_runCommand_flag():
    return runCommand_flag


def get_schedule(name):
    if name == 'cycle':
        return cycle
    elif name == 'flow1':
        return flow1
    elif name == 'flow2':
        return flow2
    elif name == 'flow3':
        return flow3
    elif name == 'area':
        return area
    elif name == 'startTime':
        return startTime
    elif name == 'stopTime':
        return stopTime
    else:
        return None