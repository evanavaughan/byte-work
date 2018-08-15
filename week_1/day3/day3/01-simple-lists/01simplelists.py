# * Input a string, using a while loop to make the user enter new strings until the length is at least 5.
string = str(input("Enter a string that is 5 characters or more: \n"))
while len(string) <= 4:
    print("It's short, but the last character in the string is '" + string[-1] + "'" )
    string = str(input("Enter a string that is 5 characters or more: \n"))
print("Great! Your string is 5 characters!")