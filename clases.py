import logging
import json

# Настройка логирования
logging.basicConfig(
    filename='HR-System/errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class Canditants:
    def __init__(self):
        self.persons = {}

    #ДОБАВЛЕНИЕ +1 К ID С КАЖДЫМ ПРИМИНЕНИЕМ
    def add_ID(self):
        self.next_id = len(self.persons)
        self.next_id += 1
        new_ID = self.next_id
        return new_ID

    #ДОБАВЛЕНИЕ ПОЛЬЗОВАТЕЛЯ
    def add_person(self, surname: str, name: str , patronymic: str, age: int, mail: str, status: str):
        try:
            new_ID = self.add_ID()
            self.persons[new_ID] = {
                "surname": surname,
                'name': name,
                "patronymic": patronymic,
                "fullname": f"{surname} {name} {patronymic}",
                'age': age,
                'mail': mail,
                'status': status,
            }
            print(f"Кандинтант с ID: [{new_ID}] добавлен!")
        except Exception as e:
            logging.error(f"Ошибка при добавлении кандидата: {e}")

    #ВЫВОД ВСЕХ ПОЛЬЗОВАТЕЛЕЙ
    def all_persons(self):
        try:
            result = ""
            print(f"🔍 Найдено {len(self.persons)} кандидата:")
            for person_id, person_info in self.persons.items():
                result += f"ID: {person_id} | Фамилия: {person_info['surname']} | Имя: {person_info['name']} | Отчество: {person_info['patronymic']} | Возраст: {person_info['age']} | E-mail: {person_info['mail']} | Статус: {person_info['status']}\n"
            if result != "":
                return result
            else:
                return "Список кандинтантов пуст!"
        except Exception as e:
            logging.error(f"Ошибка при выводе всех кандидатов: {e}")

    #ВЫВОД ПО ID
    def get_person_ID(self, ID: int):
        try:
            if ID in self.persons:
                person = self.persons[ID]
                return f"ID: {ID} | Фамилия: {person['surname']} | Имя: {person['name']} | Отчество: {person['patronymic']} | Возраст: {person['age']} | E-mail: {person['mail']} | Статус: {person['status']}"
            else:
                return f"Кандидат с ID {ID} не найден.\n─────────────────────────────────"
        except Exception as e:
            logging.error(f"Ошибка при поиске по ID: {e}")

    #ВЫВОД ПО ФИО
    def get_person_fio(self, fullname: str):
        try:
            if not fullname or len(fullname) < 2:
                return "Введите хотя бы 2 символа для поиска\n─────────────────────────────────"
            result = []
            search = fullname.lower()
            search_words = search.split()
            for ID, person in self.persons.items():
                fullname_lower = person['fullname'].lower()
                if all(word in fullname_lower for word in search_words):
                    result.append(
                        f"ID: {ID} | Фамилия: {person['surname']} | Имя: {person['name']} | Отчество: {person['patronymic']} | Возраст: {person['age']} | E-mail: {person['mail']} | Статус: {person['status']}")
            if result:
                return f"🔍 Найдено {len(result)} кандидатов:\n" + "\n".join(result)
            else:
                return f"Кандидат с ФИО '{fullname}' не найден.\n─────────────────────────────────"
        except Exception as e:
            logging.error(f"Ошибка при поиске по ФИО: {e}")

    #ФИЛЬТРАЦИЯ ПО СТАТУСУ
    def filter_by_status(self, status: str):
        try:
            filtered = [(ID, person) for ID, person in self.persons.items() if person['status'] == status]
            if not filtered:
                return f"Кандидаты со статусом '{status}' не найдены. \n─────────────────────────────────"

            result = ""
            for ID, person in filtered:
                print(f"🔍 Найдено {len(filtered)} кандидата:")
                result += f"ID: {ID} | Фамилия: {person['surname']} | Имя: {person['name']} | Отчество: {person['patronymic']} | Возраст: {person['age']} | E-mail: {person['mail']} | Статус: {person['status']}\n"
            return result
        except Exception as e:
            logging.error(f"Ошибка при фильтрации по статусу: {e}")

    #РЕДАКТИРОВАНИЕ ПОЛЬЗОВТЕЛЯ
    def edit_candidate(self, ID: int, key: str, value: str):
        try:
            if ID not in self.persons:
                return f"Кандидат с ID {ID} не найден."

            person = self.persons[ID]

            if key not in person:
                return f"Поле '{key}' отсутствует в данных кандидата."

            person[key] = value
            surname = person["surname"]
            name = person["name"]
            patronymic = person["patronymic"]
            person["fullname"] = f"{surname} {name} {patronymic}"
            return f"Поле '{key}' кандидата с ID {ID} успешно обновлено.\n─────────────────────────────────"
        except Exception as e:
            logging.error(f"Ошибка при редактировании кандидата: {e}")

    #УДАЛЕНИЕ ПОЛЬЗОВАТЕЛЯ
    def del_candidate(self, ID: int):
        try:
            if ID not in self.persons:
                return f"Кандидат с ID {ID} не найден.\n─────────────────────────────────"

            del self.persons[ID]
            return "Кандидант был удалён\n─────────────────────────────────"
        except Exception as e:
            logging.error(f"Ошибка при удалении кандидата: {e}")

    #СОХРАНЕНИЕ ПОЛЬЗОВТЕЛЕЙ
    def export_json(self):
        try:
            with open("HR-System/output.json", "w", encoding="utf-8") as f:
                json.dump(self.persons, f, indent=4)
        except Exception as e:
            logging.error(f"Ошибка при сохранении данных: {e}")

    #РАЗГРУЗКА ПОЛЬЗОВАТЕЛЕЙ
    def import_json(self):
        try:
            with open("HR-System/output.json", "r", encoding="utf-8") as f:
                pers_dict = json.load(f)
                self.persons = {int(k): v for k, v in pers_dict.items()}
        except Exception as e:
            logging.error(f"Ошибка при загрузке данных: {e}")

    #ПЕРЕМЕНАЯ ВМЕСТО СЛОВАРЯ ПО КЛЮЧУ
    def get_person(self, key:str):
        person = self.persons

        return person.get(key)


a = Canditants()