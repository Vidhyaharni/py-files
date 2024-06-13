

def expression(exp1):
    stack=[]
    for ch in exp:
        if ch in'{[(':
            stack.append(ch)
        elif ch in '}])':
            if stack[-1] == "[" and ch==']':
                stack.pop()
            elif stack[-1] == "{" and ch=='}':
                stack.pop()
            elif stack[-1] == "(" and ch==')':
                stack.pop()
            else:
                return ("false")
            
exp="({]})"           
result=expression(exp)   
if result=='false':
    print("unbalanced")   
else:
    print("balanced")    
''' 
if len(stack)==0:
    print("balanced")
else:
    print("unbalanced")
'''

