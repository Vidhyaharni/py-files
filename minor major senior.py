'''write a program to get the number of members in a family.Ask the user to enter the age of every member.
Display the number of major,minor and senior citizens. stop the execution if age is above 110.....
Note- All senior citizens are major'''

import sys
num_of_members=input("enter the total number of members present in your family:")
if num_of_members.isdigit()==False:
    print("invalid")
    sys.exit()
num_of_members=int(num_of_members)
if (num_of_members < 0 or num_of_members >=15):
    print("invalid")
    sys.exit()

major=0
minor=0
senior=0
count=1

for i in range(num_of_members):
    age=int(input(f"enter the age of member{i+1}:"))
    #if age.isdigit()==True:
    if age>=80 and age<=110:
        senior=senior+count
        major=major+count
    
    elif age <=110 and age >= 18:
        major=major+count
            
    
    elif age > 0 and age < 18:
        minor=minor+count
    
    else:
        print("invalid")
        sys.exit()
    #else:
     #   print("invalid")
      #  sys.exit()

print("minor count:",minor)
print("major count:",major)
print("senior count:",senior)
    