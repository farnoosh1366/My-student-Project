class Time:
    def __init__(self,hour,minute,second):
        self.hour= hour 
        self.minute= minute
        self.second= second 
    def __str__(self):
        if self.hour<9 :
         return f"0{self.hour}:{self.minute}:{self.second} am"   
        elif 9<self.hour<=12:
         return f"{self.hour}:{self.minute}:{self.second} am"   
        elif 21>=self.hour>12:
            return f"0{self.hour-12}:{self.minute}:{self.second} pm" 
        else:
            return f"{self.hour-12}:{self.minute}:{self.second} pm"  
a =Time(22,32,60)
print(a)
