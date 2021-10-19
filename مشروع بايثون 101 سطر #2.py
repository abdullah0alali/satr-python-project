
c_1 ={'name' :'Amal' ,'number' :1111111111}
c_2 ={'name' :'Mohammed' ,'number' :2222222222}
c_3 ={'name' :'Khadijah' ,'number' :3333333333}
c_4 ={'name' :'Abdullah' ,'number' :4444444444}
c_5 ={'name' :'Rawan' ,'number' :5555555555}
c_6 ={'name' :'Faisal' ,'number' :6666666666}
c_7 ={'name' :'Layla' ,'number' :7777777777}


def qqq ():

    a =int(input('Search for a number in PhoneBook?'))
    if a == 1111111111:
        for x in c_1.values():
            print(x)
            www()
    elif a == 2222222222:
        for x in c_2.values():
            print(x)
            www()
    elif a == 3333333333:
        for x in c_3.values():
            print(x)
            www()
    elif a == 4444444444:
        for x in c_4.values():
            print(x)
            www()
    elif a == 5555555555:
        for x in c_5.values():
            print(x)
            www()
    elif a == 6666666666:
        for x in c_6.values():
            print(x)
            www()
    elif a == 7777777777:
        for x in c_7.values():
            print(x)
            www()
    elif a < 1000000000:
        print('This is invalid number')
        www()
    elif a > 9999999999:
        print('This is invalid number')
        www()
    elif a in range(1000000000, 9999999999):
        print('Sorry, the number is not found')
        www()
    else:
        print('This is invalid number')
        www()



def www ():
    while True:
        b=input('Type "y" to search "n" to exit')
        if b == 'y':
            qqq()
        elif b =='n':
            print("Bye Bye....")
        else:
            print('Only y/n.....')
www()
