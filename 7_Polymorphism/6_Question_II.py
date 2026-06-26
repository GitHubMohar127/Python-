# Question 2

# Create two classes:

# Printer
# Scanner

# Each has:

# start()

# Write:

# def run(device):
#     device.start()

# Pass both objects.

# (This demonstrates Duck Typing.)

class Printer:
    def start(self):
        print("Printer start")

class Scanner:
    def start(self):
        print("Scanner start")

def run(device):
    device.start()

p1 = Printer()
s1 = Scanner()

run(p1)
run(s1)