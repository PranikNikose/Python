#Code1 Printing Count of Even and Odd from the User Inputed List:
list=[]
len=int(input("Enter the Length:"))

for x in range(0,len):
    x=int(input("Enter the next element:"))
    list.append(x)

print("List:",list)  #list=[2,5,7,24,74,3,43,57]

def fun(list):
    even=0
    odd=0
    for i in list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

even,odd = fun(list)

print("Even:",even)
print("Odd:",odd)

print("Even : {} and Odd : {}" .format(even,odd))





