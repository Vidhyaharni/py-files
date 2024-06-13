

rows=int(input('enter the rows:'))
columns=int(input('enter the columns:'))

for row in range(rows):
    for column in range(columns):
        if (row==column) or (row+column==rows):
            
            print('V',end='')

        else:
            print('',end='  ')
    print( )
