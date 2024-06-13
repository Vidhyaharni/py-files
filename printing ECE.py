'''printing ECE'''

size=int(input('enter the size: '))
alpha=input('enter the symbol in which each alpha needed to be printed: ')
def print_E():
    for row in range(1,size+1):
        for column in range (1,size+1):
            if column==1 or row==1 or row==size or row==size//2:
                print(alpha,end=' ')
            else:
                print('',end='')
        print(' ')
    print()       

def print_C():
    for row in range(1,size+1):
        for column in range (1,size+1):
            if column==1 or row==1 or row==size :
                print(alpha,end= ' ')
            else:
                print('',end='')
        print(' ')       
    print()

print_E()
print_C()
print_E()