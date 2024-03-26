
text = "За вікном починається весна. Перші промені сонця лагідно торкаються землі, \
пробуджуючи природу. Краплини роси блищать на молодій траві, немов діаманти. Птахи повертаються з теплих країв, \
наповнюючи повітря своїм співом. Все навколо оживає, і серце переповнюється радістю та надією на нове життя. \
Весна — це час змін, нових починань та безмежних можливостей."

#====================================================================
# Функції 1-3 було використано Безверхим Олександром
# 1. Розділення рядка на слова за допомогою методу split()
words = text.split()

# 2. Підрахунок кількості слів у тексті за допомогою функції len()
num_words = len(words)

# 3. Перетворення рядка у верхній регістр за допомогою методу upper()
uppercase_text = text.upper()

print("Вивід результатів роботи функцій split(), len() та upper():")
print("Розділення рядка на слова:", words)
print("Кількість слів у тексті:", num_words)
print("Текст у верхньому регістрі:", uppercase_text)

# Функції 4-6 було використано Зуєвою Христиною
# 4) Застосування функції Lower() - перетворення всіх символів рядка на нижній регістр
lower_text = text.lower()

# 5) Застосування функції Find() - призначена для пошуку підрядка всередині іншого рядка
findWord = "весна"
position = lower_text.find(findWord)

# 6) Застосування функції Replace() - призначена для заміни всіх входжень підрядка в рядку на інший підрядок
replaced_text = text.replace("промені", "промінці")

print("Текст змінено на нижній регістр: ", lower_text, "\n")
print("Індекс першого входження слова '",
      findWord, "' в тексті:", position, "\n")
print(replaced_text)

#====================================================================
# Функції Добродумова Нікіти Сергійовича
# Застосування функцій title(), isalpha() та isdigit()
# title() - кожне слово з великої літери
# isalpha() - чи є весь текст з букв
# isdigit() - чи є весь текст з цифр
text_title = text.title()
text_isalpha = text.isalpha()
text_isdigit = text.isdigit()
print("title() - ", text_title)
print("isaplha() - ", text_isalpha)
print("isdigit() - ", text_isdigit)

# Функції 10 - 12 було використано Тимофієм Багно
# 10 - звернення за індексом  | words[i]
# 11 - конкатенація (додавання рядків) | words[i] + '\n'
# 12 - str.join() - Збірка рядка зі списку з роздільником str | ' '.join(words)

for i in range(0, len(words)):
    if(words[i][-1] == '.'):
        words[i] = words[i] + '\n'

formated_text = ' '.join(words)

print(formated_text)

#====================================================================
# Функції Добродумова Савченка Максима
# Застосування функцій counter.most_common(), .replace(), ord()
# counter.most_common() - рахуєкількість кількість повтору унікальних символів
# .replace() - видаляє символ
# .ord() - представляй кожен символ в виді Юнікоду

import collections

texts = [text, text, text]

# 1. Вивести найчастіше зустрічаємі символи в тексті
counter = collections.Counter(texts[0])
most_common_chars = counter.most_common(5)
print("Найчастіше зустрічаємі символи:")
for char, count in most_common_chars:
    print(f"Символ '{char}' зустрічається {count} разів")

# 2. Вивести текст без пробілів
text_without_spaces = texts[1].replace(" ", "")
print("\nТекст без пробілів:\n")
print(text_without_spaces)

# 3. Представити всі символи в виді юнікоду
print("\nТекст у вигляді юнікоду:\n")
unicode_text = [ord(char) for char in texts[2]]
print(unicode_text)

formated_text = ' '.join(words)

print(formated_text)
