

size=int(input('enter the size: '))
ch=input("enter the character in which the pattern has to be printed: ")
#right angle triangle
def right_angle_triangle():
    for row in range(size):
        for col in range(row+1):
            print(ch,end=' ')
        print()
    
# inverted right angle triangle
def inverted_right_angle_triangle():
    for row in range(size):
        for col in range(size,row,-1):
            print(ch,end=' ')
        print()



print("right angle triangle")
right_angle_triangle()
print()
print('inverted right angle triangle') 
inverted_right_angle_triangle()
print()
