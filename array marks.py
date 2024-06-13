'''you have a list of student names.you have one list each for their marks in CS,math and english.
hard code the values,no need to get it as input.
pass mark is 50.
grade A is,mark 90 or above
grade B,80 or above
fail is <50
print the name of the students who got A in all subjects or atleast one A and the rest B.
try to use only one if statement'''

student_names=["sam","ram","vishnu","sreeja","lakshmi"]
cs_marks=[89,98,65,37,90]
maths_marks=[97,90,52,96,85]
eng_marks=[84,98,28,57,89]
grade_A_B=[]

count=len(student_names)
for i in range(count):
    if (cs_marks[i]>=90 and maths_marks[i]>=90 and eng_marks[i]>=90)or (cs_marks[i]>=90 and maths_marks[i]>=80 and eng_marks[i]>=80) or(cs_marks[i]>=80 and maths_marks[i]>=80 and eng_marks[i]>=90) or(cs_marks[i]>=80 and maths_marks[i]>=90 and eng_marks[i]>=80) :
        #print(f"grade A in all subjects -{student_names[i]}")
        grade_A_B.append(student_names[i])
        
print(f"grade A in all subjects or atleast in one subject -{grade_A_B}")

       


  