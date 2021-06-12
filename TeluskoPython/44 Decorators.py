#Code1 Without Using Decorator

#def div(x,y):
#    if (x<y):
#        x,y=y,x
#    print("x/y:",x/y)
#div(3,9)
#print()

#with using Decorator function under function is decorator

def div(a,b):
    print("a/b:",a/b)
def smart_div(funct):
    def inner_div(a,b):
        if a < b:
            a,b = b,a
        return funct(a,b)
    return inner_div
div = smart_div(div)
div(12,3)


