# Your Python program should perform the following four tasks:
# 1. Create a dictionary with the following elements:
# 1. “CS250” : “Business Application Programming”
# 2. “IS340” : “E-commerce”
# 3. “CS599” : “Directed Project”
# 2. After getting a word of input from the user (i.e., a string such as “IS340”) as the 
# key, your program should find the matching value and print out it. If there is no 
# matching, print out “Not Exist!” message. Note that you need to use the input 
# word as the key in the dictionary.
# 3. Receive another key and value (i.e., course number and title) from the user and 
# insert it to the dictionary.
# 4. Print out the entire dictionary to check if your insertion is correctly done.

all_words = {
    "CS250" : "Business Application Programming", 
    "IS340" : "E-commerce",
    "CS599" : "Directed Project",
    "PYTHON": "Programming Language"
} 

def banner():
    print("*************************************")
    print("\t1.Search Word")
    print("\t2.Add New Word")
    print("\t3.Update Word")
    print("\t4.Display Entire Dictionary")
    print("\t5.Exit")
    print("**************************************")

def display():
    print("Words in the dictionary")
    for key in all_words:
        print("{}:{}".format(key, all_words[key]))



while(True):
    banner()
    choice = int(input())
    if choice == 1:
        word = input("enter the word to search: ")
        if word in all_words.keys():
            print("{}:{}".format(word, all_words[word]))
        else:
            print("Word Not Found. If you wish to add the word to dictionary press 2")
    elif choice == 2:
        word = input("enter the word to add: ")
        if word in all_words.keys():
            print("{} is already there in the dictionary. \nIf you wish to update the meaning press 3".format(word))
        else:
            meaning = input("Enter the meaning of {}:".format(word))
            all_words[word] = meaning
    elif choice == 3:
        word = input("enter the word to update: ")
        if word in all_words.keys():
            meaning = input("Enter the meaning of {}:".format(word))
            all_words[word] = meaning
        else:
            print("{} is not present in dictionary. Press 2 to add".format(word))
    elif choice ==4:
        display()
    else:
        print("GoodBye!!")
        break
    