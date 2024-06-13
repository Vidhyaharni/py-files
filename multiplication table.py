'''
write a program to print multiplication tables of the number given by user.do not accept
 negative values from the user'''

num=int(input("enter a number:"))
if(num<0):
    print("invalid input")
else:
    for i in range(1,11):
      print(num,'x',i,'=',num*i)
     