import json

class Login:
    def __init__(self):
        self.admins = {}

    #ДОБАВЛЕНИЕ ПОЛЬЗОВАТЕЛЯ
    def add_admin(self, login: str, password: str, fullname: str, is_admin=False):
        self.admins[login] = {
            'password': password,
            'fullname': fullname,
            'is_admin': is_admin
        }
        self.export_admins()

    #ВХОД
    def login(self, login: str, password: str):
        from main import hr_menu
        if login in self.admins:
            if self.admins[login]['password'] == password:
                if self.admins[login]['is_admin']:
                    print(f"Добро пожаловать {self.admins[login]['fullname']}")
                    hr_menu()
                else:
                    print("Вы не администратор")
            else:
                print("Вы ввели неверный пароль!")
        else:
            print("Данного пользователя не существует!")

    #ПОДТВЕРЖДЕНИЕ ПРАВ АДМИНИСТРАТОРА
    def approved_admin(self, user_login: str):
        if user_login not in self.admins:
            print("Данного пользователя нет.")
            return
        if self.admins[user_login]['is_admin']:
            print("Данный пользователь уже администратор")
        else:
            self.admins[user_login]['is_admin'] = True
            print("Вы назначили данного пользователя админом")
            self.export_admins()

    #СОХРАНЕНИЕ АДМИНОВ
    def export_admins(self):
        with open("HR-System/admins.json", "w", encoding="utf-8") as f:
            json.dump(self.admins, f, indent=4)

    #РАЗГРУЗКА АДМИНОВ
    def import_admins(self):
        with open("HR-System/admins.json", "r", encoding="utf-8") as f:
            pers_dict = json.load(f)
            self.admins = {k: v for k, v in pers_dict.items()}
b = Login()