from random import randint

def draw_cells():
    print(f' {cell[0]} | {cell[1]} | {cell[2]}')
    print('---|---|---')
    print(f' {cell[3]} | {cell[4]} | {cell[5]}')
    print('---|---|---')
    print(f' {cell[6]} | {cell[7]} | {cell[8]}')

def check_symbol(symbol):
    if symbol in 'XOХО':
        return True
    else:
        print('[Ошибка] Выберите символ X или O')
        return False

def check_cell(number):
    if 1 <= number <= 9:
        return True
    else:
        print('[Ошибка] Введите число от 1 до 9 включительно.')
        return False

def random_cell():
    return randint(1, 9)

cell = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

symbol_flag = True
while symbol_flag:
    input_symbol = input('Выберите символ: ').upper()
    if check_symbol(input_symbol):
        if input_symbol in 'XХ':
            comp_symbol = 'O'
        elif input_symbol in 'OО':
            comp_symbol = 'X'
        symbol_flag = False

game_flag = True
while game_flag:
    step_user_flag = True
    while step_user_flag:
        input_cell = int(input('Введите номер ячейки: '))
        if check_cell(input_cell) and cell[input_cell - 1] == ' ':
            cell[input_cell - 1] = input_symbol
            step_user_flag = False
        elif cell[input_cell - 1] != ' ':
            print('[!] Выбранная ячейка занята.')

    step_comp_flag = True
    while step_comp_flag:
        input_cell = randint(1, 9)
        print(input_cell)
        if cell[input_cell - 1] == ' ':
            cell[input_cell - 1] = comp_symbol
            step_comp_flag = False

    draw_cells()


