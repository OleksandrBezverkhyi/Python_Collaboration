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
