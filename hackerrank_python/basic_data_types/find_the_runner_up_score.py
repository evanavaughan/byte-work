# Find the Second Largest Number

# You are given N numbers. Store them in a list and find the second largest number.

# Input Format 
# The first line contains N. The second line contains an array A[] of N integers each separated by a space.

# Constraints
# 2 <= N <= 10
# -100 <= A[i] <= 100

# Output Format 
# Output the value of the second largest number.

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
while arr[-1] == arr[-2]:
    del arr[-1]
print(arr[-2])