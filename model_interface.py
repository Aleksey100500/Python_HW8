import csv
from distutils import dir_util
import model_except as me
import csv
def user_interface():
    user_menu()
    number = user_choise()
    if number == 1:
        user_choise_fullcsv()
    elif number == 2:
        user_choise_sotrudnik()
    elif number == 3:
        user_choise_work()
    elif number == 4:
        user_choise_new_rab()

def user_menu():
    print('\n Выберите необходимое действие.')
    print('1. Показать все записи.')
    print('2. Поиск сотрудника по фамилии.')
    print('3. Сделать выборку сотрудников по должности.')
    print('4. Добавить нового сотрудника.')
    print('5. Обновить данные сотрудника.')
    print('6. Удалить существующую запись.')
    print('7. Закончить работу.\n')
    

def user_choise():
    vibor = me.check_number(input('Выберите пункт меню: '))
    return vibor

def user_choise_fullcsv():
    with open('BD_STO.csv', newline='') as csvfile:
        all_reader = csv.reader(csvfile, delimiter=',')
        for row in all_reader:
            print(row)

def user_choise_sotrudnik():
    surch_name = me.check_name()
    with open('BD_STO.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            row['SNFN'] = row['SNFN'].split()
            if row['SNFN'][0] == surch_name:
                print(row)

def user_choise_work():
    surch_name = me.check_work()
    with open('BD_STO.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            row['JobTitle'] = row['JobTitle'].split()
            if row['JobTitle'][0] == surch_name:
                print(row)

def surch_col():
    with open('BD_STO.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        colums = 0
        for row in reader:
            colums += 1
        return colums + 1

def name_workers():
    new_name = input('Введите ФИО сотрудника: ')
    new_name = new_name.lower()
    new_name = new_name.title()
    return new_name

def year_of_birth():
    year_f = input('Введите дату рождения в формате ДД.ММ.ГГ: ')
    return year_f

def number_of_tel():
    number_f = input('Введите номер телефона с кодом оператора в формате (375(код)..): ')
    return number_f

def education_workers():
    new_name = input('Введите образование сотрудника: ').lower()
    return new_name

def jobtitle_workers():
    new_name = input('Введите должность сотрудника: ').lower()
    return new_name

def user_choise_new_rab():
    with open('BD_STO.csv', newline='') as csvfile:
        file_writer = csv.writer(csvfile, delimiter=',')
        # first_row = surch_col()
        # second_row = name_workers()
        # file_writer.writerow([surch_col(), name_workers(), year_of_birth(), number_of_tel(), education_workers(), jobtitle_workers()])
        for row in file_writer:
            file_writer.writerow(['Null'])
            print(row)
user_interface()