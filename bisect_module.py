import bisect

a = 5

s = [1,3,4,6,7,9]

bisect.insort(s,a) #inserts a in the place where the list s is still sorted
print(s)