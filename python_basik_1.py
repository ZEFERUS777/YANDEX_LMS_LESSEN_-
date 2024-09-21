data = tuple((input().split(maxsplit=1)) for _ in range(int(input())))
one_axis = list((int(x), int(y)) for x, y in data if int(x) == 0 or int(y) == 0)

first_quarter, second_quarter, third_quarter, fourth_quarter = [], [], [], []
for cord in data:
    if int(cord[0]) > 0 and int(cord[1]) > 0:
        first_quarter.append(cord)
    elif int(cord[0]) < 0 and int(cord[1]) > 0:
        second_quarter.append(cord)
    elif int(cord[0]) < 0 and int(cord[1]) < 0:
        third_quarter.append(cord)
    elif int(cord[0]) > 0 and int(cord[1]) < 0:
        fourth_quarter.append(cord)
for x in one_axis:
    print(x)
print(f'I: {len(first_quarter)}, II: {len(second_quarter)}, III: {len(third_quarter)}, IV: {len(fourth_quarter)}.')
