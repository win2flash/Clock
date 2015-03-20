import sched, datetime, time, os
 
 
class Lesson(object):
 
    def __init__(self, start_hour, start_minute, end_hour, end_minute, number):
        self.start_time = datetime.datetime(1,1,1,start_hour,start_minute)
        self.end_time = datetime.datetime(1,1,1,end_hour,end_minute)
        self.number = number
    def is_now(self, time):
        if time > self.start_time and time < self.end_time:
            return True
        return False
 
 
class LessonAgregator(object):
   
    def __init__(self):
        self.array_lessons = []
        self.array_lessons.append(Lesson(8, 20, 9, 50, 1))
        self.array_lessons.append(Lesson(10, 05, 11, 35, 2))
        self.array_lessons.append(Lesson(12, 05, 13, 35, 3))
        self.array_lessons.append(Lesson(13, 50, 15, 20, 4))
        self.array_lessons.append(Lesson(15, 30, 17, 00, 5))
       
    def find_lesson(self, now_time):
        for lesson in self.array_lessons:
            if lesson.is_now(now_time):
                return lesson  
 
 
class ClockAgregator(object):
 
    def __init__(self):
        self.clocks = []  
        self.s = sched.scheduler(time.time, time.sleep)
    
    def add(self, clock) :
        self.clocks.append(clock)
        
    def sheduler_event(self):
	os.system('cls' if os.name=='nt' else 'clear')
        for clock in self.clocks:    
	    clock.print_time()
    
    def loop(self):
        while True:    
	    self.s.enter(0.5, 1, self.sheduler_event, ())
	    self.s.run()
                 
               
class Clock(object) :
    
    def __init__(self, lesson_agregator):
        self.lesson_agregator = lesson_agregator      
       
    def check_time(self):
        self.time = datetime.datetime.now().replace(year=1,month=1,day=1) #strftime("%H:%M:%S")
       
 
    def print_time(self):
        self.check_time()
        l = self.lesson_agregator.find_lesson(self.time)
        if l is not None:
	    print "Lesson number:" + str(l.number)
        print self.time.time().strftime("%H:%M:%S")
                  
           
class BackwardsClock(Clock):
 
    def print_time(self) :
        self.check_time()
        l = self.lesson_agregator.find_lesson(self.time)
        if l is not None:
	    print "Before end of lesson: " + str(l.end_time - self.time)[:-7]
	else:
	    print "Out of lessons"       
       
 
def main():
    lesson_agregator = LessonAgregator()
    clock_agregator = ClockAgregator()
    clock = Clock(lesson_agregator)
    backwards_clock = BackwardsClock(lesson_agregator)
    clock_agregator.add(clock)
    clock_agregator.add(backwards_clock)
    clock_agregator.loop()
    
		     
		     
if __name__ == "__main__":
    main()
