
import collections

with open("article.txt") as f:
    text = f.read()

words = re.compile(r"a-zAZ'").findall(text)
counts = collections.Counter(words)
'''
##### Objective 1 

#* Write a function that takes a filename, examines the file, and prints the most common word.
def extract(file):
    output_list = []
    cnt = collections.Counter()
    with open("article.txt", 'r') as file:
        for line in file:
            cnt[word] += 1
        print(cnt)
    
extract("article.txt")
##### Objective 2

* Write a function that takes a filename, examines the file, and prints the n most common words in
descending order.

##### Hint:

* Create your own simple file with test data

* This would be a good time for a data structure that has words for keys instead of numbers.

filename = "mbox-short.txt"

def extract(filename):
    output_list = []
    with open(filename, 'r') as filename:
        for line in filename:
            if "X-DSPAM-Confidence:" in line:
                output_list.append(line)
        return output_list

lines = extract(filename)

for index, line in enumerate(lines):
    lines[index] = float(line.split(" ")[1])

total = 0
for num in lines:
    total += num

avg = total / len(lines)
print(round(avg, 4))
'''