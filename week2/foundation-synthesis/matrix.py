def open_file(f)
    with open(filename,"r") as file_object:
        #read the file and set variable for the list1
        output_list = []
        #this len is the length of the file that was just read
        for c in range(len(output_list[0])):
            for r in range(len(output_list)):
                print("{:<}".format(output_list[r][c]), end="")
        print()
