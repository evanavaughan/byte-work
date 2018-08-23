#ANSWER

import re
filename = "mbox-short.txt"

def get_answer(filename):
    with open("mbox-short.txt", 'r') as file_object:
        _count = 0
        _sum = 0.0
        pattern = "X-DSPAM-Confidence:\s+([0-9].+)"  #anything in () will be available in result.group
        for line in file_object:
            result = re.search(pattern, line)
            if result: #means if result is not None
                value = result.groups()[0]
                _sum = _sum + float(value)
                _count = _count + 1
    print(_sum / _count)

get_answer(filename)