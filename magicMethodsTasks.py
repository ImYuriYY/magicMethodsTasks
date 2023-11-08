# TASK Vector3D
import random

# class Vector3D:
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __add__(self, other):
#         if not isinstance(other, Vector3D):
#             raise TypeError("ERROR!")
#         return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
#
#     def __sub__(self, other):
#         if not isinstance(other, Vector3D):
#             raise TypeError("ERROR!")
#         return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
#
#     def __mul__(self, other):
#         if not isinstance(other, (int,Vector3D)):
#             raise TypeError("ERROR!")
#         if isinstance(other, Vector3D):
#             return self.x * other.x + self.y * other.y + self.z * other.z
#         elif isinstance(other, int):
#             return Vector3D(self.x * other, self.y * other, self.z * other)
#
#     def __matmul__(self, other):
#         if not isinstance(other, Vector3D):
#             raise TypeError("ERROR!")
#         return Vector3D((self.y * other.z - self.z * other.y), -(self.x * other.z - self.z * other.x), (self.x * other.y - self.y * other.x))
#
#     def display(self):
#         print(f'X = {self.x}, Y = {self.y}, Z = {self.z}')
#
#     def read(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
# v1 = Vector3D(1,2,3)
# v1.display()
#
# v2 = Vector3D()
# v2.read(3,2,1)
#
# v4 = v1 + v2
# v4.display()
#
# v3 = Vector3D(4,5,6)
#
# a  = v4 * v3
# print(f'a = {a}')
#
# v4 = v1 * 10
# v4.display()
#
# v4 = v1 @ v3
# v4.display()








# TASK Прямоугольный треугольник

# class RightTriangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         self.c = (a**2 + b**2)**0.5
#
#     def reducePerc(self, side, perc):
#         if (side == "AB" or side == "BA"):
#             if (perc == 0):
#                 print(self.a)
#             else:
#                 self.a = self.a + self.a * perc / 100
#                 print(self.a)
#
#         elif (side == "AC" or side == "CA"):
#             if (perc == 0):
#                 print(self.c)
#             else:
#                 self.c = self.c + self.c * perc / 100
#                 print(self.c)
#         elif (side == "BC" or side == "CB"):
#             if(perc == 0):
#                 print(self.b)
#             else:
#                 self.b = self.b + self.b * perc / 100
#                 print(self.b)
#
#
#     def circleRadius(self):
#         print(self.c / 2)
#
#     def perimetr(self):
#         print(self.a + self.b + self.c)
#
#     def angleValue(self):
#         print(f"AB = {self.a}\nBC = {self.b}\nAC = {self.c}")
#
# rt = RightTriangle(3,4)
# rt.circleRadius()
# rt.perimetr()
# rt.angleValue()
# rt.reducePerc("BC", 20)











# TASK "Автобус"

class Bus:
    def __init__(self, speed, maxSpeed, seats):
        self.speed = speed
        self.seats = seats
        self.maxSpeed = maxSpeed
        self.capacity = len(self.seats)
        self.passengers = {}
        self.hasEmptySeats = self.capacity


    def landing(self, *args):
        if (len(args) > 1):
            for i in range(len(args)):
                busSeat = random.choice(self.seats)
                self.seats.remove(busSeat)
                self.passengers[args[i]] = busSeat
        else:
            busSeat = random.choice(self.seats)
            self.passengers[args[0]] = busSeat
            self.seats.remove(busSeat)
        self.hasEmptySeats = len(self.seats)

    def disembarkation(self, *args):
        if (len(args) > 1):
            for i in range(len(args)):
                self.seats.append(self.passengers[args[i]])
                del self.passengers[args[i]]
        else:
            self.seats.append(self.passengers[args[0]])
            del self.passengers[args[0]]
        self.hasEmptySeats = len(self.seats)

    def speedReduce(self, count):
        self.speed -= count

    def speedAdd(self, count):
        self.speed += count

    def info(self):
        print(f'Текущая скорость: {self.speed}')
        print(f'Максимальная скорость: {self.maxSpeed}')
        print(f'Максимальное количество пассажиров: {self.capacity}')
        print(f'Количество свободных мест: {self.hasEmptySeats}')
        print('Текущие пассажиры и их места:')
        arrayOfNamePassagers = list(self.passengers.keys())
        arrayOfSeatsPassagers = list(self.passengers.values())
        for i in range(len(arrayOfNamePassagers)):
            print(f'{arrayOfNamePassagers[i]} - {arrayOfSeatsPassagers[i]}')



myBus = Bus(60, 120,["A1", "A2", "B1", "B2", "B3", "C1", "C2", "C3"])
myBus.landing("Badili", "Caesar", "Alex", "Eric")
myBus.disembarkation("Badili", "Caesar")
myBus.info()
