'''get certain fruits name,count them and display them using dictionary '''

no_of_fruits=int(input('enter the number of fruits: '))
fruits_count={}
for i in range(no_of_fruits):
    fruit=input(f'enter the fruit name:  {i+1}.')
    if fruit in fruits_count:
        fruits_count[fruit]+=1
    else:
        fruits_count[fruit]=1
for fruit,count in fruits_count.items():
    print(fruit,'=',count)


    

    

    