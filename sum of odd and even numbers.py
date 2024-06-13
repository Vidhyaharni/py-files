'''Find sum of odd digits and sum of even digits in a number.for example,if the input is
58974,sum of odd digits is 5+9+7=21 and sum of even digits is 8+4=12'''

import sys
num=input("enter a number: ")
odd=0
even=0
if num.isdigit()==False:
    print("invalid input,please enter a number")
    sys.exit()
num=int(num)
if num<=0:
    print("enter a valid input")
    sys.exit()
while num > 0:
    rem=num%10
    num=num//10
    if rem%2==0:
        even=even+rem
    else:
        odd=odd+rem
print("sum of odd digits: ",odd)
print("sum of even digits: ",even)

