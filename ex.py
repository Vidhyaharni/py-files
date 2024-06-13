'''for i in range(10):
	if i == 5:
		exit()
	print(i)

name="13965784@"
if name.isdigit():
    print (" not ok")
else:
    print("ok")'''
age=input("enter the age:")
if age.isdigit()==False:
    print ("invalid input,enter you age properly")
    exit()
    
else:
    age=int(age)
    if age<1 or age>100:
        print("invalid age,please enter it again")