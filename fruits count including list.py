

no_of_fruits=int(input('enter the number of fruits:'))
#fruits_list=[]
fruits_count={}
for i in range(no_of_fruits):
    fruits=input(f'enter the fruits name:{i+1}.')
    #fruits_list.append(fruits)
#print(fruits_list)
#for fruits in fruits_list:
    if fruits in fruits_count:
        fruits_count[fruits]+=1
    else:
        fruits_count[fruits]=1
#print(fruits_count)
for fruit,count in fruits_count.items():
    print(fruit,'=',count)


    

    

    