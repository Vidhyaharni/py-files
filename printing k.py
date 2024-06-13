rows=9
columns=6
for row in range(rows):
    for column in range(columns):
        if(column==0) or (column==1 and row==4) or (column==2 and (row==3 or row==5)) or (column==3 and (row==2 or row==6)) or (column==4 and (row==1 or row==7)) or (column==5 and (row==0 or row==8)):
            
            print('4',end=' ')
        else:
            print(' ',end=' ')
    print('')
