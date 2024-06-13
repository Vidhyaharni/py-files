rows=5
columns=9
for row in range(rows):
    for column in range(columns):
        if(row==4)or (row==3 and(column==1 or column==7)) or (row==2 and (column==2 or column==6)) or (row==1 and (column==3 or column==5)) or (row==0 and column==4):
            
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print('')
