
'''In your college Python is taught in 3 different departments by the same professor. 
For each dept, get the no of students studying Python and their marks in the final exam 
Get the input as comma seperated string

Find the top 3 marks in each class
Find the top 3 marks in all classes are combined.
Find the avg mark of students with passing mark in each class and the classes combined.
Find which class has the best average mark and least number of failed students.'''

departments=3
marks=[]
stu_and_marks={}
for dept in range (departments):
    no_of_students=int(input(f"enter the number of students in department {dept+1}: "))
    print(no_of_students)
    mark=int(input("enter the marks of all the students( separate them using commas): "))
    marks=[mark]
print(marks)

'''
    stu_and_marks=int(input("enter the stu_and_marks: "))
    print(stu_and_marks)
   
    no_of_students=int(input(f"enter the number of students in department {dept+1}: "))
    marks=int(input("enter the marks of all the students( separate them using commas): "))
    print([marks])
    #print(no_of_students)'''