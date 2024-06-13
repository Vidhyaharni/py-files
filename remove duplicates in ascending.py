'''Problem #1
You have a list of numbers in ascending order, but with duplicates.
Remove the duplicated, append _ at the end for each duplicate removed 
eg input = [1,2,3,3,3,4,4,7,7,9]
output = [1,2,3,4,7,9,_,_,_,_]'''

inp=input('enter the list:' )
inpu=inp.split(',')
l2=[]
l3=[]
for i in inpu:
    if i not in l2:
        l2.append(i)
    else:
        l3.append("_")
l2.extend(l3)
print(l2)
