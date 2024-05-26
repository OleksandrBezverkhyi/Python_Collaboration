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
csv_to_json('data.csv', 'data.json')

#початковий вміст файлу data.csv:
#Name,Age,City
#Victor,20,Sumy
#Alina,19,Kyiv
#Stepan,18,Zhytomyr
#=============================================================================
