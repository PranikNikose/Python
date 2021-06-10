num= int(input("Enter a number= "))
flag = False
for x in range (2,num//2):
    if num%x == 0:
        flag = True
if flag:
    print("Not Prime")
else:
    print("Prime")
