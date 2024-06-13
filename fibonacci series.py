''' write a program to print fibonacci series of the number given by the user(if it reaches the num it will exit)'''


num=int(input("enter a number:"))
f1=0
f2=1
print(f1 )
print(f2 )
for i in range(num):
    f3=f1+f2
    f1=f2
    f2=f3
    print(f3)
    if num<=f3:
        exit()
        