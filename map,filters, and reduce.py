'''
map function

map(function to apply, list of inputs)
'''

def square(n):
    return n**2

l1 = [1,3,5,7,9]
sq = list(map(square, l1))
# print(sq)

'''
filter function
filter (function, list of inputs)
'''

def greater_than_2(n):
    return n>2

fil = list(filter(greater_than_2, l1))
# print(fil)

'''
reduce function
'''

from functools import reduce

def square(n, m):
    return n+m
red1 = reduce(square, [1,2,3,4])

print(red1)