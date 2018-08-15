# * Input a string, using a while loop to make the user enter new strings until the length is at least 5.
# * Print the 5th character, otherwise print "It's short, but the last character is <>" where <> is the last character in the string.


while True
    string = str(input("Enter a string that is 5 characters or more: \n"))
    if len(string) <= 4:
        print("It's short, but the last character in the string is '" + string[-1] + "'" )
    else:
        print("the fifth character is {}")
print("Great! Your string is 5 characters!")

# * Use slice indexing ([a:b:c] possibly with some of the values missing) to store a string that is just
# every second character.

'''
