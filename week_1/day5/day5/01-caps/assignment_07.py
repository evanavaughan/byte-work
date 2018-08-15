'''Write a program that prompts for a file name, then
opens that tfile and reads through the file, and print
the contents of the file in upper case. use the file
words.txt'''


with open('words.txt', 'r') as file_object:
    for line in file_object:
        print(line, end="")