'''Problem #2
Same as above,but print the list in descending order
input = [1,2,3,3,3,4,4,7,7,9]
output = [9,7,4,3,2,1,_,_,_,_]'''

inp=input('enter the list:' )
inpu=inp.split(',')
l2=[]
l3=[]
for i in inpu:
    if i not in l2:
        l2.append(i)
    else:
        l3.append("_")
l2=l2[::-1]
l2.extend(l3)
print(l2)