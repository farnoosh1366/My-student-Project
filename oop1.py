class Cat:
    def __init__(self,name,Sen,Nezhad):
        self.name=name
        self.sen=Sen
        self.nezhad=Nezhad
    def start (self):
            print("Cat Can walk")
    def Talk(self):
        print("Cat can Mio mio")
    def food (self):
        print("Cat can food eat")
a1=Cat("perchian -","4-","Himalin")
print(a1.name,a1.sen,a1.nezhad)
a1.start()
a1.Talk()
a1.food()