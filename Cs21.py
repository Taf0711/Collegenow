rows = int(input('How many rows?'))
cols = int(input('How many columns?'))
for row in range(rows):
    for col in range(cols):
        print('*', end='')
    print()
