
data = [0,1,2,3,4,5,6,7,8]

for item in data:
    col = (item%3)-1
    row = (item//3)-1
    print(f'Num: {item}')
    print(f'Col: {col}')
    print(f'Row: {row}')
    print()