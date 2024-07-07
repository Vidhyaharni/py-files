import mysql.connector

def connection(query):
    studentsdb = mysql.connector.connect(host="localhost",user="root",password="Bavatharini1*",database="students",)
    cursor_stu=studentsdb.cursor()
    cursor_stu.execute(query)
    return cursor_stu,studentsdb
  
def get_details(name):
    studentsdb = mysql.connector.connect(host="localhost",user="root",password="Bavatharini1*",database="students",)
    stucursor=studentsdb.cursor()
    query=f'select *from stud where name like "{name}%"'
    stucursor.execute(query)
    data=stucursor.fetchall()
    for rec in data:
        print(f'ID:{rec[0]}')
        print(f'Name:{rec[1]}')
        print(f'Gender:{rec[2]}')
        print(f'Date of birth:{rec[3]}')
        print("*******************")
        
def inserting(id,name,gender,dob):
    query=f'insert into stud(id,name,gender,dob)values{id,name,gender,dob}'
    cursor_stu,studentsdb=connection(query)
    studentsdb.commit()
    print(f"\n info inserted student:{name}")

def updating(query):
    cursor_stu,studentsdb=connection(query)
    studentsdb.commit()
    print(f"\n info updated")

print('1 - to search and display the student details\n2 - to update the student details\n3 -to insert the student details')

num = int (input('\nenter the number to perform the operation : '))
if num ==1:
    name=input('\nenter the name of the student:')
    get_details(name)
elif num==2:
    print('1- update id\n2- update name\n3- update date of birth')
    numb=int(input('\nenter the number to choose the option:'  ))
    if numb==2:
        par1=input('enter the name:')
        par2=int(input("enter the id:"))
        query=f'update stud set name="{par1}" where id={par2}'
        # updating(name,id)
    elif num==3:
        par1=input('enter the date of birth:')
        par2=int(input("enter the id:"))
        query=f'update stud set dob="{par1}" where id={par2}'
    elif num==1:
        par1=int(input("enter the old id:"))
        par2=int(input("enter the new id:"))
        
        query=f'update stud set id="{par2}" where id={par1}'

    updating(query)
elif num==3:
    id=int(input("enter the id:"))
    name=input('enter the name of the student:')
    gender=input('enter the gender of the student:')
    dob=input("enter the date of birth:")
    inserting(id,name,gender,dob)
    #didnt work
    # print("enter the values in this format : id,name,gender,date of birth ")
    # val=input('enter the values:')
    # inserting(val)





