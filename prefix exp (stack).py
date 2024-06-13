'''Problem #5
Same as above, but the operator come first.
eg - input ["+","1", "2", "*", "5"]
output =  15
explanation (1 + 2) * 5 = 15
input ["-","10", "+", "2", "3", "*", "5"]
output =  25
explanation (10 - ( 2 + 3)) * 5 = 25'''

def prefix_exp(inp):
    inp=inp[::-1]
    stack=[]
    for digit in inp:
        if digit.isdigit():
            stack.append(int(digit))
        else:
            if digit.isalpha():
                return False
            if len(stack)<2:
                inp.append(digit)
                continue
            num1=stack.pop()
            num2=stack.pop()
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
    return stack.pop()     

def output(ans):
    if ans==False:
        print("alphabets cant be calculated")
    else:
        print('output :',ans )
               
input1=["+","1", "2", "*", "5"]
print(f"the input : {input1}")
ans1=prefix_exp(input1)
output(ans1)
input2=["-","10", "+", "2", "3", "*", "5"]
print(f"the input : {input2}")
ans2=prefix_exp(input2)
output(ans2)