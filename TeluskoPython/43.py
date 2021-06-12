# Code1 with using the Function
lst=[1,2,3,4,5,6,7,8]
print("List:",lst)
def is_even(n):
    if n%2==0:
        return n

def is_odd(n):
    if n % 2 != 0:
        return n

evens = list(filter(is_even,lst))
odds = list(filter(is_odd,lst))

print("Even:",evens)
print("Odds:",odds)
print()

#Code2 Without Using The function or using Anonymous Function:

lst1=[2,4,12,17,15,9,6]
print("List:",lst1)
even1 = list(filter(lambda n: n%2==0,lst1))
print("Even1:",even1)
odd1 = list(filter(lambda n: n%2!=0,lst1))
print("Odd1:",odd1)
print()

#Code3  Filter map and Reduce
from functools import reduce as r

lst2=[1,2,3,4,5,6,7,8,9]
print("List2:",lst2)

even2=list(filter(lambda n : n%2==0,lst2))  #filter
print("Even2:",even2)

lst3 = list(map(lambda n: n*2,even2))       #map
print("Doubles:",lst3)

sum = r(lambda a,b: a+b,lst3)
print("Sum:",sum)
