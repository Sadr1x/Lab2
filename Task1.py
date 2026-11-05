class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed          

    def travel_time(self, distance):
        return distance / self.speed

    def describe(self):
        return "Транспортний засіб"

    def __str__(self):
        return f"{self.__class__.__name__}: {self.brand}, {self.speed} км/год"


class Car(Vehicle):
    def __init__(self, brand, speed, fuel):
        super().__init__(brand, speed)
        self.fuel = fuel            

    def travel_time(self, distance):
        return super().travel_time(distance) + 0.5   

    def describe(self):
        return f"Авто, {self.fuel} л/100 км"


class Bicycle(Vehicle):
    def __init__(self, brand, speed, gears):
        super().__init__(brand, speed)
        self.gears = gears

    def travel_time(self, distance):
        return super().travel_time(distance) + 1    

    def describe(self):
        return f"Велосипед, {self.gears} передач"


class Plane(Vehicle):
    def __init__(self, brand, speed, altitude):
        super().__init__(brand, speed)
        self.altitude = altitude    

    def travel_time(self, distance):
        return super().travel_time(distance) + 1.5   

    def describe(self):
        return f"Літак, висота {self.altitude} м"


vehicles = [Car("Toyota", 90, 7.5), Bicycle("Giant", 18, 21), Plane("Boeing", 800, 11000)]

print("--- Поліморфний обхід ---")
for v in vehicles:
    print(v)
    print("  ", v.describe())
    print("   Час на 600 км:", round(v.travel_time(600), 2), "год")

print("--- isinstance / issubclass ---")
print(isinstance(vehicles[0], Car))        
print(isinstance(vehicles[0], Vehicle))    
print(isinstance(vehicles[0], Plane))      
print(issubclass(Bicycle, Vehicle))        
print(issubclass(Car, Plane))              
