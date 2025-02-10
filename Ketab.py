class Ketab:
    def __init__(self,name,tedadsafe,nevisandeh):
        self.name= name
        self.tedadsafe=tedadsafe
        self.nevisandeh=nevisandeh
    def __str__(self):
         return f"Nam :{self.name},Safehat :{self.tedadsafe},Nevisandeh:{self.nevisandeh}"
if __name__=="__main__":
  a =Ketab("shahname",500,"Ferdosi")
  b=Ketab("golestan",600,"Sadi")
  print(a)
  print(b)