'''
* Write a function called ```square_list(a_list)``` that takes a list of integers as its argument

* It should print "<> squared is <>." on a line for each element in the list.

* So ```square_list([2,3,4,5])``` would output

```
2 squared is 4.
3 squared is 9.
4 squared is 16.
5 squared is 25.
'''

a_list = [2,3,4,5]
def square_list(a_list):
    for number in a_list:
        square = number * number
        print(number,"squared is", square)

square_list(a_list)
