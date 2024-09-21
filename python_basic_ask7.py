items = {
    'ножницы': ['ром', 'бумага'],
    'бумага': ['пират', 'камень'],
    'ром': ['пират', 'бумага'],
    'камень': ['ножницы', 'ром'],
    'пират': ['ножницы', 'камень'],
}

player_one, player_two = input().strip(), input().strip()
if player_one == player_two:
    print('ничья')
elif items[player_one][0] == player_two or items[player_one][1] == player_two:
    print('первый')
else:
    print('второй')