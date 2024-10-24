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
    user_number = input('Введите число: ')

    if check_input(user_number):
        if int(user_number) == random_number:
            print(f'Вы угадали загаданное число {user_number}!')
            flag_game = False
        elif int(user_number) > random_number:
            print('Ваше число больше, загаданного')
        elif int(user_number) < random_number:
            print('Ваше число меньше загаданного')
    else:
        print('[Ошибка] Введите число от 1 до 100.')