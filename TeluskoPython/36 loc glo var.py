#Code1

a=10  #global
def something():
    a=15      #local
    print("Fun",a)   #print Local

something()
print("Out",a)   #print Global
print()

#code2
b=10
def some():
    global b
    b= 20
    print("In2",b)
some()
print("Out2",b)
print()

#code3
print("Code3")
c=10 #global
def some2():
    c=15   # local
    print("In2", c)
    globals()['c'] = 3
    0   #changed global
some2()
print("Out2",c)