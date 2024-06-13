


departments=4

marks=[]
def dept():
   
        print(f"department1")
        stu_in_dept=int(input(f'enter the number of students in dept: ')) 
        #print(stu_in_dept)
        for i in range(stu_in_dept):
            mark=int(input(f'enter the mark of stu{i+1}: '))
            marks1.append(mark)
            #print(marks)
        return marks1
marks1=[]
marks2=[]
marks1=dept()
print('marks1',marks1)
marks2=dept()
print('marks2',marks2)