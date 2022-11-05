from datetime import datetime

def start_menu():
    timecalc = datetime.now().strftime('%H:%M:%S')
    with open('log_file.csv', 'a') as f:
        f.write(f'Время начала работы. {timecalc}\n')

def exit_menu():
    timecalc = datetime.now().strftime('%H:%M:%S')
    with open('log_file.csv', 'a') as f:
        f.write(f'Время окончания работы. {timecalc}\n')

def user_number_1():
    timecalc = datetime.now().strftime('%H:%M:%S')
    with open('log_file.csv', 'a') as f:
        f.write(f'Были показаны все записи из файла BD_STO. {timecalc}\n')

def user_number_2(sotrudnic):
    timecalc = datetime.now().strftime('%H:%M:%S')
    with open('log_file.csv', 'a') as f:
        f.write(f'Был произведен поиск сотрудника {sotrudnic}. {timecalc}\n')

def user_number_3(dolgnost):
    timecalc = datetime.now().strftime('%H:%M:%S')
    with open('log_file.csv', 'a') as f:
        f.write(f'Был произведен поиск сотрудника по должности - {dolgnost}. {timecalc}\n')

def user_number_4(new_sotrudnic):
    timecalc = datetime.now().strftime('%H:%M:%S')
    with open('log_file.csv', 'a') as f:
        f.write(f'Добавили нового сотрудника - {new_sotrudnic}. {timecalc}\n')

def user_number_5(new_sotrudnic):
    timecalc = datetime.now().strftime('%H:%M:%S')
    with open('log_file.csv', 'a') as f:
        f.write(f'Обновили данные сотрудника - {new_sotrudnic}. {timecalc}\n')

def user_number_6(del_sotr):
    timecalc = datetime.now().strftime('%H:%M:%S')
    with open('log_file.csv', 'a') as f:
        f.write(f'Удалили запись сотрудника - {del_sotr}. {timecalc}\n')

def new_error():
    timecalc = datetime.now().strftime('%H:%M:%S')
    with open('log_file.csv', 'a') as f:
        f.write(f'Ошибка ввода. {timecalc}\n')

def name_check(name):
    timecalc = datetime.now().strftime('%H:%M:%S')
    with open('log_file.csv', 'a') as f:
        f.write(f'Проверка имени. {name} {timecalc}\n')

def name_check(name):
    timecalc = datetime.now().strftime('%H:%M:%S')
    with open('log_file.csv', 'a') as f:
        f.write(f'Проверка должности. {name} {timecalc}\n')