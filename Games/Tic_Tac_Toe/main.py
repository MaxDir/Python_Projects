
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

input_symbol = input('Выберите символ: ').upper()
print(check_symbol(input_symbol))
