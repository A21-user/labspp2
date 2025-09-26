thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) 


thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


thisset = {"apple", "banana", "cherry"}
print(thisset)



thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)    #dd an item to a set, using the add() method:#


thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)      #remove#


#The union() and update() methods joins all items from both sets.

#The intersection() method keeps ONLY the duplicates.

#The difference() method keeps the items from the first set that are not in the other set(s).

#The symmetric_difference() method keeps all items EXCEPT the duplicates.



set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
