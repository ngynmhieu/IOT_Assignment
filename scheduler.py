from all import *

class Worker:
    def __init__(self,func, delay, period):
        
        self.worker_id = None
        self.func = func
        self.delay = delay
        self.period = period
        self.next = None

class Company:
    def __init__(self):
        self.head = None
        self.number = 0

company = Company()
worker_id = 0
time_stamp = 0
SCH_MAX_TASKS = 10
    
def SCH_Add_Task(func, delay, period):
    global worker_id
    worker = Worker(func, delay, period)
    if (func == None or delay < 0 or period < 0):
        print (f'Add task {worker_id} with delay {delay} and period {period}')
        return 0
    worker_id += 1
    worker.worker_id = worker_id
    
    if company.number >= SCH_MAX_TASKS: # full worker
        return 0
    if company.number == 0: # Empty company
        company.head = worker
        company.number += 1
        return 0
    
    current = company.head
    prev = None
    delay_temp = worker.delay - current.delay
    
    while delay_temp >= 0 and current is not None:
        worker.delay = delay_temp
        prev = current  
        current = current.next
        if current is not None:
            delay_temp -= current.delay
            
    if prev is None: # Insert at the beginning
        worker.next = current
        if current is not None:
            current.delay -= worker.delay
        company.head = worker
    elif current is None: # Insert at the end
        prev.next = worker
    else: # Insert in the middle
        prev.next = worker
        worker.next = current
        current.delay -= worker.delay
    company.number += 1
    return 0

def SCH_Delete_Task (worker_id):
    if company.number == 0:
        return 0
    
    current = company.head
    prev = None
    while current is not None:
        if current.worker_id == worker_id:
            if prev is None: # Delete at the head
                company.head = current.next
                if current.next is not None:
                    current.next.delay += current.delay
            elif current.next is None: # Delete at the end
                prev.next = None
            else: # Delete in the middle
                prev.next = current.next
                current.next.delay += current.delay
            company.number -= 1
            return 0
        prev = current
        current = current.next
    return 0

def SCH_Dispatch_Tasks():
    while company.head.delay == 0 and company.number != 0:
        # print (f'TaskID {company.head.worker_id} is running at {time_stamp}')
        company.head.func() # Run worker
        if company.head.period != 0: # periodly worker
            SCH_Add_Task(company.head.func, company.head.period, company.head.period)
        SCH_Delete_Task(company.head.worker_id) # Delete worker
        
def SCH_Update ():
    global time_stamp
    time_stamp += 1
    if company.number != 0 and company.head.delay != 0:
        company.head.delay -= 1