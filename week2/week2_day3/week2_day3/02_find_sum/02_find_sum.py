filesum = "regex_sum.txt"
filesum1 = "regex_sum_1.txt"
sum = 0


with open(filesum, 'r') as file:
   for line in file:
       sum += int(line)
print(sum)


