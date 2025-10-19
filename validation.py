import logging
import re

# Настройка логирования
logging.basicConfig(
    filename='HR-System/errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


# ВАЛИДАЦИЯ НА ВОЗРАСТ
def validation_age(age: int):
    while True:
        try:
            if age >= 15 and age <= 60:
                return age
            else:
                age = int(input("""
            [Ошибка] Вы ввели недопустимое значение! (15-60)

            Введите возраст: """))
        except ValueError as e:
            logging.error(f"Ошибка при вводе возраста: {e}")


# ВАЛИДАЦИЯ НА ПОЧТУ
allowed_domains = ['mail.ru', 'gmail.com', 'alabuga.ru', 'ya.ru', 'yandex.ru']


def validation_mail(mail: str):
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


# ВАЛИДАЦИЯ НА СТАТУС
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


# ВАЛИДАЦИЯ НА ПАРОЛЬ
def validation_password(password: str):
    if len(password) < 8:
        logging.error("Ошибка: Длина пароля должна быть не менее 8 символов.")
        return False
    return True