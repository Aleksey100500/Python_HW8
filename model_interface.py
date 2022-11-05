import model_except as me
import csv
import model_log as mlog

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
    elif number == 5:
        user_choise_update_new()
    elif number == 6:
        user_delete(me.check_name())
    elif number == 7:
        mlog.exit_menu()
        user_exit()
        


def user_menu():
    print('\n Выберите необходимое действие.')
    print('1. Показать все записи.')
    print('2. Поиск сотрудника по фамилии.')
    print('3. Сделать выборку сотрудников по должности.')
    print('4. Добавить нового сотрудника.')
    print('5. Обновить данные сотрудника.')
    print('6. Удалить существующую запись.')
    print('7. Закончить работу.\n')


def user_exit():
    exit()


def user_delete(surch_name):
    with open('BD_STO.csv', 'rt') as csvfile:
        reader = csv.reader(csvfile)

        with open('new_BD_STO.csv', 'wt') as csvfile:
            writer = csv.writer(csvfile)
            for line in reader:
                if surch_name in line[1]:
                    line = []
                writer.writerow(line)
                print(line)
    mlog.user_number_6(surch_name)
    user_interface()


def user_choise():
    vibor = me.check_number(input('Выберите пункт меню: '))
    return vibor


def user_choise_fullcsv():
    with open('BD_STO.csv', newline='') as csvfile:
        all_reader = csv.reader(csvfile, delimiter=',')
        for row in all_reader:
            print(row)
    mlog.user_number_1()
    user_interface()


def user_choise_sotrudnik():
    surch_name = me.check_name()
    with open('BD_STO.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            row['SNFN'] = row['SNFN'].split()
            if row['SNFN'][0] == surch_name:
                print(row)
    mlog.user_number_2(surch_name)
    user_interface()
    return surch_name


def user_choise_work():
    surch_name = me.check_work()
    with open('BD_STO.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            row['JobTitle'] = row['JobTitle'].split()
            if row['JobTitle'][0] == surch_name:
                print(row)
    mlog.user_number_3(surch_name)
    user_interface()


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
    year_f = input('Введите дату рождения в формате ДД.ММ.ГГГГ: ')
    return year_f


def number_of_tel():
    number_f = input(
        'Введите номер телефона с кодом оператора в формате (375(код)..): ')
    return number_f


def education_workers():
    new_name = input('Введите образование сотрудника: ').lower()
    return new_name


def jobtitle_workers():
    new_name = input('Введите должность сотрудника: ').lower()
    return new_name


def user_choise_new_rab():
    with open('BD_STO.csv', 'a') as csvfile:
        calc = surch_col()
        new_name = name_workers()
        birth = year_of_birth()
        tel_num = number_of_tel()
        ed_wor = education_workers()
        job_tit = jobtitle_workers()
        csvfile.write('\n{},{},{},{},{},{}'.format(
            calc, new_name, birth, tel_num, ed_wor, job_tit))
        print('Записано.')
    mlog.user_number_4(new_name)


def user_choise_update_new():
    old_name = user_choise_sotrudnik()
    print('Что нужно обновить: \n')
    print('1. Фамилию.')
    print('2. Год рождения.')
    print('3. Номер телефона.')
    print('4. Образование.')
    print('5. Должность.')
    with open('BD_STO.csv', 'rt') as csvfile:
        data = csvfile.read()
        user_update_menu_1 = user_choise()
        if user_update_menu_1 == 1:
            with open('BD_STO.csv', 'wt') as csvfile:
                new_name = me.check_name()
                data = data.replace(f'{old_name}', f'{new_name}', 1)
                csvfile.write(data)

        elif user_update_menu_1 == 2:
            print('Текущий.')
            old_year = year_of_birth()
            with open('BD_STO.csv', 'wt') as csvfile:
                print('На который хотите заменить.')
                new_year = year_of_birth()
                data = data.replace(f'{old_year}', f'{new_year}')
                csvfile.write(data)

        elif user_update_menu_1 == 3:
            print('Текущий.')
            old_tel = number_of_tel()
            with open('BD_STO.csv', 'wt') as csvfile:
                print('На который хотите заменить.')
                new_tel = number_of_tel()
                data = data.replace(f'{old_tel}', f'{new_tel}')
                csvfile.write(data)

        elif user_update_menu_1 == 4:
            print('Текущий.')
            old_education = education_workers()
            with open('BD_STO.csv', 'wt') as csvfile:
                print('На который хотите заменить.')
                new_education = education_workers()
                data = data.replace(f'{old_education}', f'{new_education}')
                csvfile.write(data)

        elif user_update_menu_1 == 5:
            print('Текущий.')
            old_jobtitle = jobtitle_workers()
            with open('BD_STO.csv', 'wt') as csvfile:
                print('На который хотите заменить.')
                new_jobtitle = jobtitle_workers()
                data = data.replace(f'{old_jobtitle}', f'{new_jobtitle}')
                csvfile.write(data)

        else:
            print('Вы вернулись в гланое меню.')
        user_interface()
    mlog.user_number_5(new_name)


user_interface()
