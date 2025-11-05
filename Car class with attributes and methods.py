class Car: 
    def __init__(self, make, model, year): 
        self.make = make 
        self.model = model 
        self.year = year 
    def start(self): 
        print(f"Car Started: {self.make} {self.model} ({self.year})") 
    def stop(self): 
        print(f"Car Stopped: {self.make} {self.model} ({self.year})") 
car1 = Car("Supra", "MK4", 1982)  
car2 = Car("Dodge", "challenger", 1987) 
car1.start() 
car1.stop() 
car2.start() 
car2.stop()