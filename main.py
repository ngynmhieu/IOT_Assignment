from all import *
from scheduler import *

def timer_callback(): #set timer to 1 second
    SCH_Update()
    threading.Timer(1.0, timer_callback).start()
    
def task1():
    print ("Task 1")
def task2():
    print ("Task 2")
def task3():
    print ("Task 3")
    
threading.Timer(1.0, timer_callback).start()
    
SCH_Add_Task(task1, 0, 2)
SCH_Add_Task(task2, 0, 3)
SCH_Add_Task(task3, 0, 4)

while True:
    SCH_Dispatch_Tasks()
