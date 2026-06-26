#class Vector:

#    def __init__(self, values):
#        self.values = values

#    def add(self, other):
#        pass

#    def subtract(self, other):
#        pass

#    def dot(self, other):
#        pass

#    def magnitude(self):
#        pass

import math


class Vector:

    def __init__(self, values):
        self.values = values

    def add(self, other):

        result = []

        for a,b in zip(self.values, other.values):
            result.append(a+b)

        return Vector(result)


    def magnitude(self):
        total = 0

        for value in self.values:
            total += value ** 2

        return math.sqrt(total)
    
    def dot(self, other):

        total = 0

        for a,b in zip(self.values, other.values):
            total += a*b

        return total

#Magnitude
a = Vector([5, 6, 7])
# print(a.magnitude())

#Addation & Dot Product
b = Vector([0.2,0.8,0.1])
c = Vector([0.3,0.7,0.2])

d = b.add(c)
print(d.values)

print(b.dot(c))