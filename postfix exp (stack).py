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


def postfix_exp(inp):
    stack=[]
    for digit in inp:
        if digit.isdigit():
            stack.append(int(digit))
        else:
            if digit.isalpha():
                return False
            num2=stack.pop()
            num1=stack.pop()
            if digit =='+':
                output=num1+num2
                stack.append(output)
            elif digit =='-':
                output=num1-num2
                stack.append(output)
            elif digit =='*':
                output=num1*num2
                stack.append(output)
            elif digit =='/':
                output=num1/num2
                stack.append(output)
    if len(stack)!=1:
        print('invalid input')
    else:
        return stack.pop()  

def output(ans):
    if ans==False:
        print("alphabets cant be calculated")
    else:
        print('output :',ans )
         
input1=["1", "2", "+", "5", "*"]
print(f"the input : {input1}")
ans1=postfix_exp(input1)
output(ans1)
input2=["10", "2", "3", "+","-", "5", "*"]
print(f"the input : {input2}")
ans2=postfix_exp(input2)
output(ans2)





    
   


