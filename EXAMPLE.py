second_name=input("enter your second name(use uppercase):")
second_name= second_name.strip()
if (len(second_name)>3 and second_name.isalpha()==True and second_name.isupper()==True ):
    print("your second name is ",second_name)
else:
    print("invalid name,please enter it again")
    exit()
first_name=input("enter your first name(use uppercase):")
first_name= first_name.strip()
if (len(first_name)>3 and first_name.isalpha()==True and first_name.isupper()==True ): #isalnum() can also be used but it wont check the special symbols($#@) instead i am checking whether the string is filled with alphabets or not.
    print("your first name is ",first_name)
else:
    print("invalid name,please enter it again")