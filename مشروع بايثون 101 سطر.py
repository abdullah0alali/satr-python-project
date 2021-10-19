phonebook={0:{'name':'Abdullah','number':'1111111111'},
           1:{'name':'Ali','number':'2222222222'},
           2:{'name':'Ahmed','number':'3333333333'},
           3:{'name':'Seed','number':'4444444444'},
           4:{'name':'Morad','number':'5555555555'}}

def qqq ():
    n = (input('Search For Name in the Phone Book Enter --[[Name]]-- '))
    if n == 'Abdullah':
        print(phonebook[0])
        print(ggg())
    elif n == 'Ali':
        print(phonebook[1])
        print(ggg())
    elif n == 'Ahmed':
        print(phonebook[2])
        print(ggg())
    elif n == 'Seed':
        print(phonebook[3])
        print(ggg())
    elif n == 'Morad':
        print(phonebook[4])
        print(ggg())
    else:
        print('Sorry!!')
        print(ggg())


def ggg():
    g = input('search for a number or quit y/n')
    if g == 'y':
        print(qqq())
    elif g == 'n':
        print('Bye Bye!!')
    else:
        print('ONLY "y" or "n"')
        print(ggg())
ggg()
