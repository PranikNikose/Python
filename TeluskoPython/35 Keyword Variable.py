#
def person(name,*data):
    print(name)
    print(data)
person('Pranik',21,'Amravati',7058187989)


#Code2

def person1(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person1('Pranik',21,'Amravati',7058187989)