number = 0
number2 = 5
user_password = 2222

while number <= 5:
    password_please_message = int(input('Немедленно введи мне правильный пароль: '))
    if password_please_message == user_password:
        print('Путь в Нарнию открыт!')
        break
    else:
        number += 1
        if number <= 5:
           print ('Это твоя {}-я попытка из {}-ти! Попробуй ввести еще раз!'.format(number,number2))
        else:
           number == 5
           print ('Это была твоя последняя попытка!')