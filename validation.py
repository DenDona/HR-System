#ВАЛИДАЦИЯ НА ВОЗРАСТ
def validation_age(age: int):
    while True:
            if age >= 15 and age <= 60:
                return age
            else:
                age = int(input("""
            [Ошибка] Вы ввели недопустимое значение! (15-60)
                    
            Введите возраст: """))

#ВАЛИДАЦИЯ НА ПОЧТУ
allowed_domains = ['mail.ru', 'gmail.com', 'alabuga.ru', 'ya.ru', 'yandex.ru']
def validation_mail(mail: str):
    import re
    pattern = r'^[\w\.-]+@([\w\.-]+\.\w{2,})$'
    while True:
        match = re.match(pattern, mail)
        if match and match.group(1) in allowed_domains:
            return mail
        else:
            mail = input("""
[Ошибка] Вы ввели неверный E-mail!

Список доступных:
1. @mail.ru
2. @gmail.com
3. @alabuga.ru
4. @ya.ru
5. @yandex.ru

Введите E-mail: """).strip()

#ВАЛИДАЦИЯ НА СТАТУС
def validation_status(status: str):
    list_status = ["new", "interviewed", "rejected", "hired"]
    while True:
        valid = False
        for stat in list_status:
            if stat in status:
                valid = True
                break
        if valid:
            return status
        else:
            status = input("""
[Ошибка] Вы ввели неверный статус!
            
Список статусов:
1. new
2. interviewed
3. rejected
4. hired
            
Введите статус: """).strip()


#ВАЛИДАЦИЯ НА ПАРОЛЬ
def validation_password(password: str):
    while True:
        if len(password) >= 8:
            return password
        else:
            password = input("""
Введите пароль от 8 симвалов: """)