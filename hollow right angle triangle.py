rows=7
columns=7
for row in range(rows):
    for column in range(columns):
        if(row==column) or (column==0) or( row==6):
            
            print('o',end='  ')
        else:
            print(' ',end='  ')
    print('')
