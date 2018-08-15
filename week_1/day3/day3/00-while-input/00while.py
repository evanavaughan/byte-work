"""
* Ask the user to input integers or 'done', if they print an integer print that integer converted to a float

"""
userinput = input("Please give me a number or the word 'done':\n")
while userinput != "done":
    print('{:.2f}'.format(float(userinput)))
    userinput = input("Please give me a number or the word 'done':\n")
print("done")






