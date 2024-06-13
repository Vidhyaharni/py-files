'''Accept a number and find out if it is armstrong number. HINT - number should be equal to sum
of cube of digits.then it is called armstrong number.'''


num=int(input("enter a number:"))
print("the given number is: ",num)
count=len(str(num))
#print(count)
number=num
a=0
b=0
sum=0

for i in range(count):
    a=num%10
    num=num//10
    print(a)
    b=a*a*a
    sum=sum+b
    
    print(sum)
  
if (number==sum):
    print("the given number is an armstrong number")
else:
    print("the given number is not an armstrong number")    




