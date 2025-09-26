thislist = ["apple", "banana", "cherry"]
print(thislist)

#List items are indexed, the first item has index [0], the second item has index [1] etc.#


thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) 
#A list is an ordered collection of items (can be strings, numbers, or other objects).#



thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#To determine how many items a list has, use the len() function#


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]



#Python lists can store strings, numbers, or boolean values — all in the same way#


list1 = ["abc", 34, True, 40, "male"]



mylist = ["apple", "banana", "cherry"]
print(type(mylist))   #In Python, type(object) tells you what type of data the object is.#

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.#



thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #index start with 0#


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])    #Negative indexes let you slice from the end of the list just like from the beginning#

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)  



thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)  #The insert() method inserts an item at the specified index:#



thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)