students_grades = {
    "group_number": 101,
    "students": {
        "1": {
            "last_name": "Петренко",
            "first_name": "Петро",
            "middle_name": "Петрович",
            "course": 2,
            "subjects": {
                "Математика": 95,
                "Фізика": 88,
                "Хімія": 92
            }
        },
        "2": {
            "last_name": "Іваненко",
            "first_name": "Іван",
            "middle_name": "Іванович",
            "course": 3,
            "subjects": {
                "Математика": 78,
                "Фізика": 85,
                "Хімія": 80
            }
        }
    }
}

#=============================================================================================================================
# Функцію додавання було створено Безверхим Олександром

# Функція для додавання даних про нового студента до словника
def add_student_data(students, student_id, last_name, first_name, middle_name, course, subjects):
    if student_id not in students["students"]:
        students["students"][student_id] = {
            "last_name": last_name,
            "first_name": first_name,
            "middle_name": middle_name,
            "course": course,
            "subjects": subjects
        }
        print(f"Інформацію про студента {last_name} {first_name} {middle_name} було успішно додано.")
    else:
        print("Студент з таким ID вже існує.")

add_student_data(students_grades, "3", "Степаненко", "Степан", "Степанович", 1, {"Математика": 82, "Фізика": 79, "Хімія": 88})

print(students_grades)
#=============================================================================================================================
# =============================================================================================================================
# Функцію видалення було створено Зуєвою Христиною

# Функція для видалення даних студента за прізвищем

def delete_by_lastname(students, last_name):    
    for student_id, student_Dates in list(students["students"].items()):# Перебираємо студентів і видаляємо того, чий ключ "last_name" співпадає з введеним прізвищем
        if student_Dates["last_name"] == last_name:      
            del students["students"][student_id]   # видалення за індексом студента у словнику
            print(f"Студента з прізвищем {last_name} видалено.")
            return
   
    print(f"Студента з прізвищем {last_name} не знайдено.") # Якщо прізвище не знайдено

print("Введіть прізвище студента для видалення: ")
StudLastname = input()
delete_by_lastname(students_grades, StudLastname)

print(students_grades)
# =============================================================================================================================
# Функція пошуку у словнику. Створив - Добродумов Нікіта Сергійович
def find_student_by_lastname(students, last_name):
    found_students = []
    for student_id, student_data in students["students"].items():
        if student_data["last_name"] == last_name:
            found_students.append(student_data)

    if found_students:
        print(f"Знайдено студентів з прізвищем {last_name}:")
        for student in found_students:
            print(
                f"ID: {student_id}, Прізвище: {student['last_name']}, Ім'я: {student['first_name']}, По-батькові: {student['middle_name']}, Курс: {student['course']}, Предмети та оцінки: {student['subjects']}")
    else:
        print(f"Студентів з прізвищем {last_name} не знайдено.")


print("Введіть прізвище студента для пошуку: ")
StudLastname = input()
find_student_by_lastname(students_grades, StudLastname)
# =============================================================================================================================
# Функція знаходження середнього балу та виведення його в спадаючому порядку. Створив — Савченко Максим
def calculate_average_grades(students_grades):
    averages = []

    for student in students_grades["students"].values():
        average_grade = sum(student["subjects"].values()) / len(student["subjects"])
        averages.append((student["last_name"], student["first_name"], student["middle_name"], average_grade))

    averages.sort(key=lambda x: x[-1], reverse=True)

    for last_name, first_name, middle_name, average_grade in averages:
        print(f"{last_name} {first_name} {middle_name}: {average_grade:.2f}")
