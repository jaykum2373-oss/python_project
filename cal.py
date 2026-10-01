# make calculator
print('WELOCME TO CALCULATOR')
print("for addition press:1")
print("for minus press:2")
print("for multiplication press:3")
print("for division press:4")

choice=int(input('Enter your choice :'))
while True:
    if choice==1:
        x=float(input("Enter your 1st no. :"))
        y=float(input("Enter your 2nd no. :"))
        sum=x+y
        print(f"{x} + {y} = {sum}")
        choice=int(input('Enter your choice :'))    
    elif choice==2:
        x=float(input("Enter your 1st no. :"))
        y=float(input("Enter your 2nd no. :")) 
        diff=x-y
        print(f"{x} - {y} = {diff}")
        choice=int(input('Enter your choice :'))
    elif choice==3:
        x=float(input("Enter your 1st no. :"))
        y=float(input("Enter your 2nd no. :"))
        prod=x*y
        print(f"{x} * {y} = {prod}")
        choice=int(input('Enter your choice :'))
    elif choice==4:
        x=float(input("Enter your 1st no. :"))
        y=float(input("Enter your 2nd no. :"))
        d=x/y
        print(f"{x} / {y} = {d}")
        choice=int(input('Enter your choice :'))
    elif choice==5:
        print("THANK YOU " )
        break
    else:
        print("something went worng...")
        choice=int(input('Enter your choice :'))
        continue        
