import mysql.connector

def get_details():

  studentsdb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Bavatharini1*",
    database="students"
  )
  stucursor=studentsdb.cursor()
  stucursor.execute(query)
  data=stucursor.fetchall()
  # for rec in data:
  #     name=rec[1]
  #     id=rec[0]
  #     values.append(name)
  return data
#print(data)
print('1-> to search and display the student details')
print('2-> to update the student details')
print('3-> to delete the student details')
num = int (input('enter the number to perform the operation : '))
if num ==1:
  name=input('enter the name of the student:')
  query=f'select *from stud where name like "{name}"'
elif num==2:
  print('1-> to update the id')
  print('2-> to update the name')
  print('3-> to update the dob')
  num = int (input('enter the number to perform the operation : '))
  if num==1:
    old_id=int(input('enter the old id of the student:'))
    new_id=int(input('enter the new id of the student:'))
    query=f'update stud set id={new_id} where id={old_id}'
  elif num==2:
    id=int(input('enter the id of the student:'))
    name=input('enter the name of the student:')
    query=f'update stud set name="{name}" where id={id}'
  elif num==3:
    id=int(input('enter the id of the student:'))
    dob=input('enter the dob of the student:')
    query=f'update stud set dob={dob} where id={id}'
  

elif num==3:
  query=''
n=get_details()
print(n)
