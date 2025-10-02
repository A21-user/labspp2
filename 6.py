def reverse_words():
    s = input("Enter a sentence: ")
    words = s.split()            
    reversed_words = words[::-1]   
    result = " ".join(reversed_words)  
    return result

print(reverse_words())
