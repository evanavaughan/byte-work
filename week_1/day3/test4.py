rows = []
for rowindex in range(0,100,10):
    row = []
    for columnindex in range(0,10):
        row.append(rowindex + columnindex)
    rows.append(row)

for row in rows:
    for element in row:
        print("{:<3}".format(element), end="")
    # print with no argument just prints a newline character
    print()

print()
print("fifth row, seventh column is {}".format(rows[4][6]))