import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

r = float(input("Enter radius of sphere: "))
print("Volume of sphere:", sphere_volume(r))
