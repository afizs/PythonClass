# After getting a word of input from the user (i.e., any string), 
# your program should use a while (or for) loop to print out each of 
# the letters of the word. Just remember that strings in Python start with element 0!

#Python HomeWork -1 

# Your program should then use another loop to print out each of the letters of the 
# (same) word in reverse order!

word = input("Enter Your word: ")
count = 0 

length = len(word)-1

while(length>=0):
    print(word[length])
    length -= 1







