class Car(object):
    def __init__(self,model,color,company,speedlimit):
        self.model=model
        self.color=color
        self.company=company
        self.speedlimit=speedlimit
    
    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accerelate(self):
        print("accerelating")

audi=Car("A6","red","Aude","100")
print(audi.color)
audi.stop()
