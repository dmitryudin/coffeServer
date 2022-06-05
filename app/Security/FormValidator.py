# is_acceptable_password
'''
- пароль должен быть больше чем 8
- пароль должен содержать одну хотя бы одну цифру, но не состоять только из цифр
- пароль не должен иметь в своём составе "password"
- пароль должен иметь три и более различных символа
'''


def len_pass(password: str, len_word):  # проверка длинны пароля
    return len(password) >= len_word


def have_digit(password: str, ):  # проверка на наличие цифры.
    for c in password:
        if c.isdigit() == True:
            return True
    return False


def various_symbols(password: str):  # проверка на 3 неповторяющихся символа в пароле
    password = set(password)
    return len(password) >= 3


def is_acceptable_password(password: str) -> bool:
    password = password.lower()

    if len_pass(password, 8) == True:
        if have_digit(password) == True:
            if password.isnumeric() == False:
                if password.find('password') == -1:
                    if various_symbols(password) == True:
                        return True
                    else:
                        print('пароль должен иметь три и более различных символа')
                else:
                    print('не должен иметь в своём составе "password"')
            else:
                print('пароль не должен состоять только из цифр')
        else:
            print('пароль должен содержать одну хотя бы одну цифру')
    else:
        print('пароль должен быть больше чем 8')
    return False


# is_acceptable_tel_number
'''
- номер телефона должен начинаться с 8'
- номер телефона содержит 11 цифр

'''


def is_acceptable_tel_number(tel_number: str) -> bool:
    if len_pass(tel_number, 11) == True:
        if tel_number[0] == '8':
            return True
        else:
            print('номер телефона должен начинаться с 8')

    else:
        print('номер телефона содержит 11 цифр')


# is_acceptable_tel_number
'''
- должен содержать @'

- должен содержать точку'.'

'''


def is_acceptable_email(email: str) -> bool:
    if email.find('@') != -1:
        if email.find('.') != -1:
            return True
        print('некоректный эл.адресс')
    else:
        print('некоректный эл.адресс')


#a = is_acceptable_password('')
#b = is_acceptable_tel_number('89833624697')
#c = is_acceptable_email('maximgol500@ma.ilru')
