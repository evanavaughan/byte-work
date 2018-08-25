#items = [1, 2, 3, 4, 5]
#squared = list(map(lambda x:x**2, items))
#print(squared)

N=int(raw_input())
list=list(set(map(int,raw_input().strip().split(" "))))
list.sort(reverse=True)
print(list[1])
