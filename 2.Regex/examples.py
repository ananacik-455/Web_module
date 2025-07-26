import re

# text = "Привіт, світ! Це тестовий рядок."
#
# pattern = r"світ"
#
# result = re.search(pattern, text)
#
# print(result.start())
# print(result.end())
# print(text[result.start(): result.end()])


# text2 = "Номер телефону: 123-456-7890 або 987-654-3210."

# pattern_2 = r"([1234567890]{3})-([0-9]{3})-(\d{4})"

# [1234567890]{3} | [0-9]{3}  -> 3 числа

# result = re.search(pattern_2, text2)
# print(result.group(0))
# # for ()
# for i in range(1, 4):
#     print(result.group(i))

# pattern_2 = r"[1234567890]{3}-[0-9]{3}-\d{4}"
# # without grouping
# result = re.findall(pattern_2, text2)
# print(result)
# for phone_num in result:
#     print(tuple(phone_num.split("-")))

# text3 = "Python - чудова мова програмування."
# text4 = "Мова програмування: Python."
#
# pattern4 = r"Python"
# result = re.match(pattern4, text3)
#
# if result:
#     print(result.group(0))
# else:
#     print("Not matched")

# text5 = "Email: test@example.com, support@domain.org, info@mail.net."
#
# # pattern = r"\b([A-Za-z0-9._-]+)@(\w+\.[a-z]{2,3})\b" \w
# pattern = r"\b[A-Za-z0-9._-]+@\w+\.[a-z]{2,3}\b"
# # \w <-> [A-Za-z0-9_]
# result = re.findall(pattern, text5)
# print(result)

# text7 = "Ціни: $10.50, $25.00, $5.99."
# pattern = r"\$(\d+\.\d{2})"
#
# result = re.finditer(pattern, text7)
#
# for match_obj in result:
#     print(match_obj.group(0))
#     print(float(match_obj.group(1)))


# text8 = "Я люблю програмувати на Python. Python - це круто!"
# pattern = r"Python"
# replacement = "HTML"
#
# result = re.sub(pattern, replacement, text8)
# print(f"Original: {text8}")
# print(f"After replacement: {result}")
#
# result, replacement_count = re.subn(pattern, replacement, text8)
# print(f"Original: {text8}")
# print(f"After replacement: {result}")
# print(f"Number of replacement: {replacement_count}")

# text11 = "один, два; три.   чотири"
#
# pattern = r"[,.;]\s*"
#
# result = re.split(pattern, text11)
# print(result)

# long_text = "Це довгий текст з багатьма словами. Слово, слово, слово. Шукаємо слово."
# compiled_pattern = re.compile(r"\bслово\b", re.IGNORECASE)
#
# result = compiled_pattern.findall(long_text)
# print(result)

text15 = "Ім'я: Іван, Вік: 30. Ім'я: Вадим, Вік: 26."

pattern = r"Ім'я: (?P<name>\w+), Вік: (?P<age>\d+)"

result = re.finditer(pattern, text15)
dict_result = {}
for i, match_obj in enumerate(result):
    name = match_obj.group("name")
    age = int(match_obj.group("age"))
    dict_result[i] = {"name": name, "age":age}

print(dict_result)




