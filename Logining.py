from classeslogin import b
from validation import validation_password

b.import_admins()

#ВХОД И РЕГИСТРАЦИЯ
def Login_in_system():
    while True:
        login_in = input("""
──────────────────────────────────────────────────────
                 Вход в HR-Систему
──────────────────────────────────────────────────────
    
1. Войти
2. Зарегестрироваться
3. Выйти
    
Введите значение (1-3): """)

        if login_in == '1':
            login = input("""
Введите "Exit" Чтобы выйти
Введите логин: """).strip()
            if login == 'Exit':
                Login_in_system()
            password = input("""
Введите пароль: """)
            b.login(login, password)
        elif login_in == '2':
            login = input("""
Введите "Exit" Чтобы выйти
Введите логин: """).strip()
            if login == 'Exit':
                Login_in_system()
            password = input("""
Введите пароль: """)
            validation_password(password)
            fullname = input("""
Введите ФИО: """)
            b.add_admin(login, password, fullname)
            print("""
Админ скоро подтвердит вас!

Отпишитесь в Telegram админимтрации:
1. @DenDona""")
        elif login_in == '3':
            print("Вы вышли.")
            break


Login_in_system()