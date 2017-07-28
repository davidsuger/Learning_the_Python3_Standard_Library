class Car:
    pass

class Truck(Car):
    pass

c= Car()
t= Truck()
print(type(c))
print(type(t))
print(isinstance(c,Car))
print(isinstance(t,Truck))
print(isinstance(t,Car))