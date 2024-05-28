#=============================================================================
#Код написаний Безверхим Олександром

import csv
import json

def csv_to_json(csv_file, json_file):
    try:
        # Відкриваємо CSV файл для читання
        with open(csv_file, 'r', newline='') as csvfile:
            # Використовуємо DictReader для зчитування CSV файлу
            csv_reader = csv.DictReader(csvfile)
            
            # Читаємо дані з CSV і конвертуємо до списку словників
            data = []
            for row in csv_reader:
                data.append(row)
            
            # Записуємо дані у JSON файл
            with open(json_file, 'w') as jsonfile:
                json.dump(data, jsonfile, indent=4)
            
            print(f"Дані успішно сконвертовано з {csv_file} у {json_file}")
    
    except FileNotFoundError:
        print(f"Помилка: файл {csv_file} не знайдено")
    except IOError:
        print(f"Помилка: не вдалося зчитати або записати дані у файли")
    except Exception as e:
        print(f"Помилка: {str(e)}")

# Конвертація
#csv_to_json('data.csv', 'data.json')

#початковий вміст файлу data.csv:
#Name,Age,City
#Victor,20,Sumy
#Alina,19,Kyiv
#Stepan,18,Zhytomyr
#=============================================================================
#Код написаний Савченко Максимом

def write_to_csv(file_name, data):
    # file_name - рядок, що містить ім'я файлу, наприклад 'data.csv'
    # data - список словників, де ключі - це заголовки стовпців
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

# Приклад використання функції
data_to_write = [
    {'name': 'John', 'age': 30, 'city': 'New York'},
    {'name': 'Anna', 'age': 25, 'city': 'London'},
    {'name': 'Peter', 'age': 35, 'city': 'Berlin'}
]

write_to_csv('new_data.csv', data_to_write)

cvs_to_json("new_data.csv", "new_data_by_Savchenko.json")

# Вміст файлу new_data_by_Savchenko.csv має наступну структуру:
# "name": "Peter",
# "age": "35",
# "city": "Berlin"
#=============================================================================
#Код написаний Нікітою Добродумовим

def json_to_csv(json_file_path, csv_file_path):
    try:
        # Читання даних з JSON файлу
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        
        # Перевірка, що дані є списком словників
        if not isinstance(data, list):
            raise ValueError("Очікувався список словників в JSON файлі")
        
        if not all(isinstance(item, dict) for item in data):
            raise ValueError("Всі елементи JSON повинні бути словниками")

        # Отримання заголовків (ключів словників)
        headers = set()
        for item in data:
            headers.update(item.keys())
        headers = list(headers)

        # Запис даних у CSV файл
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

        print(f"Дані успішно конвертовані з {json_file_path} до {csv_file_path}")
    
    except FileNotFoundError:
        print(f"Файл {json_file_path} не знайдено.")
    except json.JSONDecodeError:
        print(f"Файл {json_file_path} не є валідним JSON.")
    except ValueError as ve:
        print(f"Помилка: {ve}")
        
def write_to_json_file(file_name, data):
    try:
        # Читання існуючих даних з файлу
        with open(file_name, 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
        
        # Перевірка, що існуючі дані є списком
        if not isinstance(existing_data, list):
            raise ValueError("Очікувався список в JSON файлі")

        # Додавання нових даних до існуючих
        existing_data.extend(data)

        # Запис оновлених даних назад у файл
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=4)

    except FileNotFoundError:
        # Якщо файл не знайдено, створити новий файл і записати дані
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except json.JSONDecodeError:
        print(f"Файл {file_name} не є валідним JSON.")
    except ValueError as ve:
        print(f"Помилка: {ve}")

data_to_write = [
    {'name': 'Ivan', 'age': 20, 'city': 'Sumy'},
    {'name': 'Mahmut', 'age': 35, 'city': 'Dubai'},
    {'name': 'Yasuke', 'age': 19, 'city': 'Tokio'}
]

write_to_json_file('new_data_by_Savchenko.json', data_to_write)

json_to_csv('new_data_by_Savchenko.json', 'new_data_by_Dobrodumov.csv')

# вміст файлу new_data_by_Dobrodumov.csv:
#age,name,city
#30,John,New York
#25,Anna,London
#35,Peter,Berlin
#30,John,New York
#25,Anna,London
#35,Peter,Berlin
#20,Ivan,Sumy
#35,Mahmut,Dubai
#19,Yasuke,Tokio
