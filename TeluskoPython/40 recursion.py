import sys as s
print(s.getrecursionlimit())
s.setrecursionlimit(2000)
print(s.getrecursionlimit())
i=0
def greet():
    global i
    i+=1
    print("Hello",i)
    greet()

greet()