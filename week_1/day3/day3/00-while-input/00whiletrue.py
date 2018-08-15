#Using while True and a break statement



while True:
    userinput = input("Please give me a number or the word 'done':\n")
    if userinput == "done":
        print("done")
        break
    else:
        print('{:.2f}'.format(float(userinput)))
        break


### not printing line 9
