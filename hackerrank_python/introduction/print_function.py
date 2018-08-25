#Read an integer .
#Without using any string methods, try to print the following:
#Note that "" represents the values in between.

#Input Format
#The first line contains an integer .

#Output Format
#Output the answer as explained in the task.

#Sample Input 0
#3
#Sample Output 0
#123

'''
n = int(input())
x = str(n)

while n > 0:
    x = str(x), str(x-1)
    print(x)
    n = n-1

n = int(input())
arr = list(map(int, input().rstrip().split()))
string = ""
for i in reversed(arr):
    string += (str(i) + " ")
print(string)
'''
array = [20, 30, 40, 50]
print(reversed(array))
