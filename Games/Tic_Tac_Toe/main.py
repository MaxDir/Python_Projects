
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
    input_cell = int(input('Введите номер ячейки: '))
    cell[input_cell] = input_symbol
    draw_cells()


