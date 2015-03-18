import sched, datetime, time, os
s = sched.scheduler(time.time, time.sleep)
 
x = 1      

def cls():
    os.system('cls' if os.name=='nt' else 'clear') 
       
def print_time():
    global x
    frame_null1 = "+ MLGclock -"
    frame_null2 = "- MLGclock +"
    frame1 = "-+-+-+-+-+-+"
    frame2 = "+-+-+-+-+-+-"
    time = datetime.datetime.now().strftime("%H:%M:%S")
    time1 = "- "  + datetime.datetime.now().strftime("%H:%M:%S") + " +"
    time2 = "+ "  + datetime.datetime.now().strftime("%H:%M:%S") + " - "
    
    
    if x == 1 :
        cls()
        print frame1
        print frame_null1
        print time1
        print frame2
        x = 0
    else:
        cls()
        print frame2
        print frame_null2
        print time2
        print frame1
        x = 1
     
 
def clock():
    while True :
        s.enter(1, 1, print_time, ())
        s.run()
clock()