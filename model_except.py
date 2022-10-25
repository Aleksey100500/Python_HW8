def check_number(number):
    try:
        number = int(number)
        print('Всё верно.')
        return number
    except ValueError:
        print('Это не число, попробуйте снова.')
        return check_number(input('Выберите пункт меню: '))


def check_name():
    surch_name = str(input('Введите фамилию сотрудника: '))
    surch_name = surch_name.lower()
    surch_name = surch_name.title()
    return surch_name