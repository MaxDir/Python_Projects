from random import randint


def check_input(string):
    if string.isdigit() and 1 <= int(string) <= 100:
        return True
    else:
        return False


print('Игра угадай число')
print('Загадано число от 1 до 100')

random_number = randint(1, 100)
print(random_number)

flag_game = True
while flag_game:
    user_number = int(input('Введите число: '))
    if user_number == random_number:
        print(f'Вы угадали загаданное число {user_number}!')
        flag_game = False
    elif user_number > random_number:
        print('Ваше число больше, загаданного')
    elif user_number < random_number:
        print('Ваше число меньше загаданного')