#الف:یک تابع خصوصی با  دوتا یا یکی _ نام گداری میشود که داده خصوصی میگویند
#ب:باید از دوتابع get ,setبرای دسترسی استفاده کرد 
class Carprid:
    def __init__(self,model,noe,masrafsokht,meghdarfeli) :
         if meghdarfeli<10 and masrafsokht >120 :
            raise "it is not safar"
         else:
            self._model =model
            self._noe=noe
            self._masrafsokht=masrafsokht 
            self._meghdarfeli=meghdarfeli
    def get_move(self):
        return self._meghdarfeli 
    def set_move(self,newmasraf ):
        if meghdarfeli <10:
              raise "it is not safar "
        else:
            self.__Maxspeed= newspeed
a1=Car("Benz",400,"c500")
print(a1.__dict__)
print(a1.get_speed())
a1.set_speed(320)#taghir midahim sorato bayad az tabeh estefadeh kard
print(a1.get_speed())#hatnam bararye seda zadane tabe () in bashad
a1._

a1=Home(160,97,3) 
print(a1.__dict__)