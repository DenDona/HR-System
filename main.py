from clases import a
from validation import validation_age, validation_mail, validation_status
from classeslogin import b

a.import_json()
print("Приветствую данные загружены!")
def hr_menu():
    while True:
        choice_mode = input("""
────────────────────────
•	Главное меню:
──────────────────────────────────────────────────────
        🎯 HR-СИСТЕМА: Управление кандидатами
──────────────────────────────────────────────────────
        
[1] Добавить кандидата
[2] Просмотреть всех кандидатов
[3] Найти кандидата (по ID или ФИО)
[4] Фильтровать по статусу
[5] Редактировать кандидата
[6] Удалить кандидата
[7] Сохранить данные
[8] Загрузить данные
[9] Подтвердить пользователя
[0] Выход
        
Выберите действие (1-9): """).strip()
        print("""
─────────────────────────────────""")

        #ДОБАВЛЕНИЕ ПОЛЬЗОВАТЕЛЯ
        if choice_mode == "1":
            surname = input("""
Введите "Exit" если хотите выйти.
Введите фамилию: """).strip().capitalize()
            if surname == "Exit":
                print("Вы вышли.")
                hr_menu()
            print("""─────────────────────────────────""")
            name = input("""
Введите имя: """).strip().capitalize()
            print("""─────────────────────────────────""")
            patronymic = input("""           
Введите отчество: """).strip().capitalize()
            print("""─────────────────────────────────""")
            age = input("""
Введите возраст (15-60): """).strip()
            age = validation_age(age)
            print("""─────────────────────────────────""")
            mail = input("""
Введите E-mail: """).strip()
            mail = validation_mail(mail)
            print("""─────────────────────────────────""")
            status = input("""
Введите статус: """).strip()
            status = validation_status(status)
            print("""─────────────────────────────────""")
            a.add_person(surname, name, patronymic, age, mail, status)

        #ВЫВОД ВСЕХ ПОЛЬЗОВАТЕЛЕЙ
        elif choice_mode == "2":
            print(a.all_persons())

        #НАХОДИТЬ ПО ФИО И ID
        elif choice_mode == "3":
            search_id_fio = input("""
Введите "Exit" если хотите выйти.

[1] Поиск по ID
[2] Поиск по ФИО
            
Выберите действие (1-2): """).strip()
            print("─────────────────────────────────")

            if search_id_fio == "1":
                search_id = int(input("Введите ID: ").strip())
                print(a.get_person_ID(search_id))
            elif search_id_fio == "2":
                search_fio = input("Введите ФИО: ").strip()
                print(a.get_person_fio(search_fio))
            elif search_id_fio == "Exit":
                print("Вы вышли.")
                hr_menu()

        #ФИЛЬТРАЦИЯ ПО СТАТУСУ
        elif choice_mode == "4":
            search_status = input("""
Введите "Exit" если хотите выйти.            

[1] new
[2] interviewed
[3] rejected
[4] hired
            
Выберите статус (1-4): """).strip()
            print("─────────────────────────────────")
            if search_status == "1":
                print(a.filter_by_status("new"))
            elif search_status == "2":
                print(a.filter_by_status("interviewed"))
            elif search_status == "3":
                print(a.filter_by_status("rejected"))
            elif search_status == "4":
                print(a.filter_by_status("hired"))
            elif search_status == "Exit":
                print("Вы вышли.")
                hr_menu()

        #РЕДАКТИРОВАНИЕ ПОЛЬЗОВАТЕЛЯ
        elif choice_mode == "5":
            ID = input("""
Введите "Exit" если хотите выйти.
Введите ID: """).strip()
            if ID == "Exit":
                print("Вы вышли.")
                hr_menu()
            if ID.isdigit():
                ID = int(ID)
            else:
                print("Вы ввели не число: ")
            print("""
─────────────────────────────────""")
            person = a.persons[ID]
            print(f"""
─────────────────────────────────
Текущие данные кандидата:    
Фамилия: {person['surname']}
Имя: {person['name']}
Отчество: {person['patronymic']}
Возраст: {person['age']}
E-mail: {person['mail']}
Статус: {person['status']}
─────────────────────────────────
    """)
            key = input("""
[1] Фамилия
[2] Имя
[3] Отчество
[4] Возраст
[5] E-mail
[6] Статус
            
Введите что хотите изменить (1-6): """).strip()
            print("""
─────────────────────────────────""")

            if key == "1":
                value = input("Введите значение: ").strip()
                print(a.edit_candidate(ID, "surname", value))
            elif key == "2":
                value = input("Введите значение: ").strip()
                print(a.edit_candidate(ID, "name", value))
            elif key == "3":
                value = input("Введите значение: ").strip()
                print(a.edit_candidate(ID, "patronymic", value))
            elif key == "4":
                value = input("Введите значение: ").strip()
                validation_age(value)
                print(a.edit_candidate(ID, "age", value))
            elif key == "5":
                value = input("Введите значение: ").strip()
                print(a.edit_candidate(ID, "mail", value))
            elif key == "6":
                value = input("Введите значение: ").strip()
                print(a.edit_candidate(ID, "status", value))

        #УДАЛЕНИЕ ПОЛЬЗОВТЕЛЯ
        elif choice_mode == "6":
            ID = int(input("""
Введите "0" если хотите выйти.
Введите ID: """))
            print(a.del_candidate(ID))

        #СОХРАНЕНИЕ ДАННЫХ
        elif choice_mode == "7":
            a.export_json()
            print("Данные выгружены.")
            print("─────────────────────────────────")

        #РАЗГРУЗКА ДАННЫХ
        elif choice_mode == "8":
            a.import_json()
            print("Данные загружены.")
            print("─────────────────────────────────")

        #ПОДТВЕРЖДЕНИЕ АДМИНИСТРАЦИИ
        elif choice_mode == "9":
            login = input("Введите логин пользователя: ").strip()
            b.approved_admin(login)

        #ВЫХОД
        elif choice_mode == "0":
            a.export_json()
            print("До свидания!")
            break

