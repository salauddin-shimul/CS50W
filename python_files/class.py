'''class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
p = Point(3, 9)
print(p.x)
print(p.y)'''

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []
    
    def add_passenger(self, name):
        if self.open_seats() == 0:
            return False
        self.passenger.append(name)
        return True
               
    def open_seats(self):
        return self.capacity - len(self.passenger)
        
flight_1 = Flight(3)
