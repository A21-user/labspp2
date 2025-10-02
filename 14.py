import math

def fahrenheit_to_celsius(f):
    return (5/9) * (f - 32)

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def sphere_volume(r):
    return (4/3) * math.pi * r**3

print("100 F in Celsius:", round(fahrenheit_to_celsius(100), 2))
print("Is 'madam' palindrome?", is_palindrome("madam"))
print("Sphere volume radius=3:", round(sphere_volume(3), 2))
