'''
syntax:
lamba_variable: manipulate(argument)

'''

add = lambda x,y: x+y

# print(add(1,2))

a = [(1,2),(4,6),(5,3)]

a.sort(key= lambda x:x[1])
# print(a)