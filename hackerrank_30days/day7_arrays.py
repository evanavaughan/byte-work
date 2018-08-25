n = int(input())
arr = list(map(int, input().rstrip().split()))
string = ""
for i in reversed(arr):
    string += (str(i) + " ")
print(string)