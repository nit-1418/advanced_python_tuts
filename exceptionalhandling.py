try:
    open("this.txt")
    print("this vlock will try to execute some code snippets. If not able to do so it will throw and exception and go to exception block.")
except Exception as e:
    print(e)
    print("this code block will throw every exception")
else:
    print("this code will run if there is no exception and the try block is successfully executed.")
finally:
    print("This code wil be executed no materr what happens in above blocks!!!")