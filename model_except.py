import model_log as mlog

def check_number(number):
    try:
        number = int(number)
        print('Всё верно.')
        return number
    except ValueError:
        print('Это не число, попробуйте снова.')
        mlog.new_error()
        return check_number(input('Выберите пункт меню: '))


def check_name():
    surch_name = str(input('Введите фамилию сотрудника: '))
    surch_name = surch_name.lower()
    surch_name = surch_name.title()
    mlog.name_check(surch_name)
    return surch_name

def check_work():
    surch_name = str(input('Введите должность сотрудника: '))
    surch_name = surch_name.lower()
    mlog.name_check(surch_name)
    return surch_name