# class Demo:
#     def add(self, a):
#         return a
#     def add(self, a, b):
#         return a+b
class Demo:
    def add(self, a, b=0):
        return a + b

d1 = Demo()

print(d1.add(2,3))

print(d1.add(2))