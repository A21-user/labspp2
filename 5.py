from itertools import permutations

def print_permutations():
    s = input("Enter a string: ")
    perms = permutations(s)   
    for p in perms:
        print("".join(p))

print_permutations()
