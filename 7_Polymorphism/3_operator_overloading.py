# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

#     def dispaly(self):
#         print(f"({self.x}, {self.y})")

# p1 = Point(2, 3)
# p2 = Point(3, 4)

# p3 = p1 + p2

# p3.dispaly()

class Demo:
    def add(self, a, b=0):
        return a + b

d1 = Demo()

print(d1.add(2))