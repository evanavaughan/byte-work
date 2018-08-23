"""
results = []
for outer_variable in outer_sequence:
    for inner_variable in inner_sequence:
        results.append



newgroup = [0, 0, 0]
for element in groupxyz:
    if (x + y + z) != z:
        newgroup.append([0, 0, 0])
print(newgroup)
"""
x = int(input("x?"))
y = int(input("y?"))
z = int(input("z?"))
n = int(input("n?"))
newgroup = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i+j+k) != n:
                newgroup.append([i, j, k])
print(newgroup)

"""
x = int ( raw_input())
y = int ( raw_input())
n = int ( raw_input())
ar = []
p = 0
for i in range ( x + 1 ):
    for j in range( y + 1):
        if i+j != n:
            ar.append([])
            ar[p] = [ i , j ] p+=1
print ar
"""