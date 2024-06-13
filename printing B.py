
rows=7
columns=5

for row in range(rows):
    for column in range (columns):
        if(column==0) or (row==0) or(row==3) or (row==6) or ((row==1 or row==2 or row==4 or row==5) and(column==4)):
            print('*',end=' ')
        else:
            print(' ',end='  ')
    print('')