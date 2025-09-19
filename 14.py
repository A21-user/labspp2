print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')



#a string in Python is just text data that your program can use, modify, and analyze.#

a = "Hello"
print(a)



#You can assign a multiline string to a variable by using three quotes#


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)




#string arrays#

a = "Hello, World!"
print(a[1])     #n Python, indexing starts at 0.#


for x in "banana":    #ake each character of the string "banana" one by one and assign it to the variable x.#
  print(x)    #prints the current character stored in x#




  a = "Hello, World!"
print(len(a))   
 #len(a) returns the number of characters in the string a.#
#This includes letters, spaces, punctuation, symbols  everything counts.#


b = "Hello, World!"
print(b[2:5])




b = "Hello, World!"
print(b[-5:-2])


a = "Hello, World!"
print(a.lower()) #lower case#   



#strip() removes spaces from both ends#
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"