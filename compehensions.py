'''
List comprehensions

Dictionary comprehensions

Set comprehensions

Generator Comprehensions
'''

list_ = [1, 2, 3, 4, 56, 46, 474, 54 ,4546, 47, 6454, 33]
d2 = [x for x in list_ if x%2 == 0] #list comprehension
# print(d2)

#dict comprehension

dict1 = {
    "a" : 12,
    "b" : 23,
    "A" : 28,
}

#print({k.lower() : dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0) for k in dict1.keys()})
# print({k : dict1.get(k) for k in dict1.keys()})

#set comprehenson

sq = {x**2 for x in [1,2,2,3,4,5,6,7,7,7,7]}
# print(sq)

#generator comprehension

gen = (i for i in range(10))
for i in gen:
    print(i)