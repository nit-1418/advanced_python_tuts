# *args and **kwargs tutorials
# *vars and **kvars

def print_name(*args): # *args is tuple type data
    if len(args) == 3: 
        print("The name of student is", args[0],"roll is",  args[1],"and percentage", args[2])
    else:
        print("The name of student is", args[0],"roll is",  args[1])

print_name("Shlok", 1)


def printmarks(**marks): #**kwargs is dictionary  type of data
    for key, value in marks.items():
        print(key,value)


marklist = {
    "Shlok": 100,
    "Sumit": 97,
    "Harry": 89,
    "Jiya": 90,
}

printmarks(**marklist)