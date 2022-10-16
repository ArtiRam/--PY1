list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
new_list = []
# TODO Оформить решение
for row in list_numbers:
    if row == 90:
        row = 25
    elif row == 25:
        row = 90
    new_list.append(row)
print(new_list)
