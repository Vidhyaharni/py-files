'''Problem #3 
Add two number represented in a list as reversed. print the sum also as a list in reverse order
eg input list1 = [1,2,3] list2 = [5,6,7]
answer= [6,8,0,1]
 explanation (321 + 765 = 1086)'''

l1 = [1,2,3] 
l2 = [5,6,7]
s=0
for i in l1:
    s=add(i)
print(s)
s1=l1[len(l1)::-1]
print(s1)
