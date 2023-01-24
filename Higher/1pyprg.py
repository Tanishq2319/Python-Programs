class vechicle:
    def __init__(self,name,max_speed,capacity):
        self.name=name
        self.max_speed=max_speed
        self.capacity=capacity
car=vechicle("audi",200,5)
print(car.name)
print(car.max_speed)
print(car.capacity)