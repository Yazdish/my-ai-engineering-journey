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


    def magnitude(self):
        total = 0

        for value in self.values:
            total += value ** 2

        return math.sqrt(total)



v = Vector([3,4])

print(v.magnitude())