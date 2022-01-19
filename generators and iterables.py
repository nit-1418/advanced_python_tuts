'''
iterable


iterator


iteration

generators are one-time iterator i.e. they can be iterate for only one time and give value for once
'''

def gen(n): #the generator function that generates n numbers
    for i in range(n):
        yield i

ob1 = gen(10)

# print(next(ob1))
# print(next(ob1))
# print(next(ob1))
# print(next(ob1))

# iterables
a = "SHLOK"

iter1 = iter(a)

# print(next(iter1))
# print(next(iter1))
# print(next(iter1))


