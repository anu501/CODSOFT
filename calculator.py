a=int(input("enter first number:"))
b=int(input("enter second number:"))
ch=0
while ch<5:
    print("calculator menu")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.exit")
    ch=int(input("enter user choice:"))
    if ch==1:
        c=a+b
        print("sum of two numbers is:",c)
    elif ch==2:
        c=a-b
        print("difference of two numbers is:",c)
    elif ch==3:
        c=a*b
        print("multiplication of two numbers is:",c)
    elif ch==4:
        c=a/b
        print("division of two numbers is:",c)
    elif ch==5:
        break
    else:
        print("invalid opeartion")
