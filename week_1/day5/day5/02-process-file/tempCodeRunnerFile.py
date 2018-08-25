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