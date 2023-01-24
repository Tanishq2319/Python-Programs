class vechicle():
    def __init__(self,name,max_capacity,speed):
        self.name=name
        self.max_capacity=max_capacity
        self.speed=speed
class bus(vechicle):
    def fare(self):
        default_fare=self.max_capacity*100
        total_fare=default_fare+(default_fare*0.1)
        return total_fare
final=bus("auto",12,50)
print(final.fare())