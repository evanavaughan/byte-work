'''
import re

def add_numbers (file):
    with open(file, 'r') as openfile:
        _sum = 0
        for line in openfile:
            pattern = "[0-9]+"
            result = re.findall(pattern, line)
            if result != None:
                _sum += _sum(result)
        return _sum

print(add_numbers("regex_sum.txt"))
print(add_numbers("regex_sum_1.txt"))   


#second method
import re

def add_numbers (file):
    with open(file, 'r') as openfile:
        _sum = 0
        for line in openfile:
            pattern = "[0-9]+"
            result = re.findall(pattern, line)
            if result != None:
                for intstring in result:
                    _sum = _sum + int(instring)
        return _sum

print(add_numbers("regex_sum.txt"))
print(add_numbers("regex_sum_1.txt"))  

'''
import re

def add_numbers (file):
    with open(file, 'r') as openfile:
        _sum = 0
        for line in openfile:
            pattern = "[0-9]+"
            result = re.findall(pattern, line)
            if result is not None:
                _sum = _sum + [int(st) for st in result]
        return _sum

print(add_numbers("regex_sum.txt"))
print(add_numbers("regex_sum_1.txt"))  
