import logging
from clases import a
from validation import validation_age, validation_mail, validation_status
from classeslogin import b

# Настройка логирования
logging.basicConfig(
    filename='HR-System/errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

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

        # ДОБАВЛЕНИЕ ПОЛЬЗОВАТЕЛЯ
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
            age = int(input("""
Введите возраст (15-60): """).strip())
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
            try:
                a.add_person(surname, name, patronymic, age, mail, status)
            except Exception as e:
                logging.error(f"Ошибка при добавлении кандидата: {e}")

        # ВЫВОД ВСЕХ ПОЛЬЗОВАТЕЛЕЙ
        elif choice_mode == "2":
            try:
                print(a.all_persons())
            except Exception as e:
                logging.error(f"Ошибка при выводе всех кандидатов: {e}")

        # НАХОДИТЬ ПО ФИО И ID
        elif choice_mode == "3":
            search_id_fio = input("""
Введите "Exit" если хотите выйти.

[1] Поиск по ID
[2] Поиск по ФИО

Выберите действие (1-2): """).strip()
            print("─────────────────────────────────")

            if search_id_fio == "1":
                search_id = int(input("Введите ID: ").strip())
                try:
                    print(a.get_person_ID(search_id))
                except Exception as e:
                    logging.error(f"Ошибка при поиске по ID: {e}")
            elif search_id_fio == "2":
                search_fio = input("Введите ФИО: ").strip()
                try:
                    print(a.get_person_fio(search_fio))
                except Exception as e:
                    logging.error(f"Ошибка при поиске по ФИО: {e}")
            elif search_id_fio == "Exit":
                print("Вы вышли.")
                hr_menu()

        # ФИЛЬТРАЦИЯ ПО СТАТУСУ
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
                try:
                    print(a.filter_by_status("new"))
                except Exception as e:
                    logging.error(f"Ошибка при фильтрации по статусу 'new': {e}")
            elif search_status == "2":
                try:
                    print(a.filter_by_status("interviewed"))
                except Exception as e:
                    logging.error(f"Ошибка при фильтрации по статусу 'interviewed': {e}")
            elif search_status == "3":
                try:
                    print(a.filter_by_status("rejected"))
                except Exception as e:
                    logging.error(f"Ошибка при фильтрации по статусу 'rejected': {e}")
            elif search_status == "4":
                try:
                    print(a.filter_by_status("hired"))
                except Exception as e:
                    logging.error(f"Ошибка при фильтрации по статусу 'hired': {e}")
            elif search_status == "Exit":
                print("Вы вышли.")
                hr_menu()

        # РЕДАКТИРОВАНИЕ ПОЛЬЗОВАТЕЛЯ
        elif choice_mode == "5":
            ID = input("""
Введите "0" если хотите выйти.
Введите ID: """).strip()
            if ID == "0":
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
                try:
                    print(a.edit_candidate(ID, "surname", value))
                except Exception as e:
                    logging.error(f"Ошибка при редактировании фамилии: {e}")
            elif key == "2":
                value = input("Введите значение: ").strip()
                try:
                    print(a.edit_candidate(ID, "name", value))
                except Exception as e:
                    logging.error(f"Ошибка при редактировании имени: {e}")
            elif key == "3":
                value = input("Введите значение: ").strip()
                try:
                    print(a.edit_candidate(ID, "patronymic", value))
                except Exception as e:
                    logging.error(f"Ошибка при редактировании отчества: {e}")
            elif key == "4":
                value = input("Введите значение: ").strip()
                validation_age(value)
                try:
                    print(a.edit_candidate(ID, "age", value))
                except Exception as e:
                    logging.error(f"Ошибка при редактировании возраста: {e}")
            elif key == "5":
                value = input("Введите значение: ").strip()
                try:
                    print(a.edit_candidate(ID, "mail", value))
                except Exception as e:
                    logging.error(f"Ошибка при редактировании почты: {e}")
            elif key == "6":
                value = input("Введите значение: ").strip()
                try:
                    print(a.edit_candidate(ID, "status", value))
                except Exception as e:
                    logging.error(f"Ошибка при редактировании статуса: {e}")

        # УДАЛЕНИЕ ПОЛЬЗОВТЕЛЯ
        elif choice_mode == "6":
            ID = int(input("""
Введите "0" если хотите выйти.
Введите ID: """))
            try:
                print(a.del_candidate(ID))
            except Exception as e:
                logging.error(f"Ошибка при удалении кандидата: {e}")

        # СОХРАНЕНИЕ ДАННЫХ
        elif choice_mode == "7":
            try:
                a.export_json()
                print("Данные выгружены.")
                print("─────────────────────────────────")
            except Exception as e:
                logging.error(f"Ошибка при сохранении данных: {e}")

        # РАЗГРУЗКА ДАННЫХ
        elif choice_mode == "8":
            try:
                a.import_json()
                print("Данные загружены.")
                print("─────────────────────────────────")
            except Exception as e:
                logging.error(f"Ошибка при загрузке данных: {e}")

        # ПОДТВЕРЖДЕНИЕ АДМИНИСТРАЦИИ
        elif choice_mode == "9":
            login = input("Введите логин пользователя: ").strip()
            try:
                b.approved_admin(login)
            except Exception as e:
                logging.error(f"Ошибка при подтверждении администратора: {e}")

        # ВЫХОД
        elif choice_mode == "0":
            try:
                a.export_json()
                print("До свидания!")
            except Exception as e:
                logging.error(f"Ошибка при выходе: {e}")
            break