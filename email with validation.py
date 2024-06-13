'''
#getting the first name
first_name=input("enter your first name(use uppercase): ")
first_name= first_name.strip()
if (len(first_name)>=3 and first_name.isalpha()==True and first_name.isupper()==True ): #isalnum() can also be used but it wont check the special symbols($#@) instead i am checking whether the string is filled with alphabets or not.
    print("your first name is ",first_name)
else:
    print("invalid name,please enter it again")
    exit()

 #getting the second name 
second_name=input("enter your second name (use uppercase): ")
second_name= second_name.strip()
if (len(second_name)<3 or second_name.isalpha()==False or second_name.isupper()==False or second_name.isdigit()==True): #
    print("invalid name,please enter it again")
    exit()
else: 
    print("your second name is ",second_name)
 ''' 
 #getting the age   
age=input("enter your age: ")
if age.isdigit()==False:
    print ("invalid input")
    exit()
age=int(age)
if age<1 or age>100:
    print("invalid age,please enter it again")
else:
    print("your age is ",age)
    '''

#getting the phone number
phone_number=input("enter your phone number: ")    
if phone_number.isdigit()==False:
     print ("invalid input")
     exit()
phone_number=int(phone_number)
if len(phone_number)==10:
    print("your phone number is ",phone_number)
else:
     print("invalid number")

 #getting the email   
email=("enter your email address:")'''