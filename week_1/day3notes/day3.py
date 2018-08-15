# while
"""
i = False
while not i:
    print('once')
    i = True

while True:
    imp = input()
    if imp == "done":
        break
"""

"""
# list - sequence type
#   sequence types: string, tuple, list
li = [1, 2, 3, 4, 5]

# print(l1[2])
# print(len(l1))
# print(l1[5])
print(li)
li[3] = 8
print(li)

li.append(10)
print(li)
x = li.pop()
print(li)
print(x)

for element in li:
    print(element)

result = []
for i in range(5):
    result.append(i * 2)
print(result)

for i in range(3):
    for j in range(2):
        print(i, j)
"""

"""
rows = []
for r in range(3):
    row = []
    for c in range(2):
        row.append(r + c)
    rows.append(row)

for row in rows:
    for element in row:
        print("{:<3}".format(element), end="")
    print()

# append, pop

# mutable vs. immutable
"""
"""
t = [1, 2, 3]
print(t[1])
t[1] = 4
print(t[1])
"""

"""
li = [1, 2]
k = [1, 2]

print(li == k)
print(li is k)
"""

"""

# list comprehension
li = [i * 2 for i in range(10)]
print(li)


li = [i * 2 for i in range(10) if i % 3 != 0]
print(li)

answer = []
for i in range(10):
    if i % 3 != 0:
        answer.append(i * 2)

"""
"""
output = " - ".join(['a', 'b', 'c'])
print(output)
"""

# output = " - ".join([1, 2, 3]) error, requires strings
# print(output)
li = [1, 2, 3]
print([str(e) for e in li])
# str(1) = '1'
output = " - ".join([str(e) for e in li])

# building lists with for

# if time: list comprehensions
# .join