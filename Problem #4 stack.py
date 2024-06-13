'''Problem #4
Input is an array of strings of an arithmetic expression. Calculate the value.
eg - input ["1", "2", "+", "5", "*"]
output =  15
explanation (1 + 2) * 5 = 15

input ["10", "2", "3", "+","-", "5", "*"]
output =  25
explanation (10 - ( 2 + 3)) * 5 = 25
Hint : Use the concept of stack. Push and pop. 
Parse the input list one element at a time. Convert to integer, push it to a stack. Whenever you see an
operator, pop two elements from the stack, apply the operation and push the result back.'''

l1=[]
l2=[]
input=["10", "2", "3", "+","-", "5", "*"]
print (input)
for ele in input:
    #if ele== '+' or ele== '-':
        ele=int(ele)
l2.append(ele)
        
    #else:
       # ele=int(ele)
        #l1.append(ele)
print(l2)
#print(l1)

