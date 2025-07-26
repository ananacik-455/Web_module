import re
from cgitb import reset

# task_text_1 = "Я вивчаю python. Python - це круто!"
#
# pattern = r"python" # your code
#
#
# result = re.findall(pattern, task_text_1, re.IGNORECASE) # ["python", "Python"]
# print(result)


# task_text_2_1 = "https://www.google.com"
# task_text_2_2 = "www.google.com"
#
# # Перевірте, чи рядок починається з "https://".
#
# pattern = r"https://"
#
# result = re.match(pattern, task_text_2_1)
# # result = re.match(pattern, task_text_2_2)
# if result:
#     print(result.group(0))
# else:
#     print("Not matched")

# task_text_3 = "Температура: 25.51 градусв. Тиск: 1012.3 гПа. Швидкість: -1.2 м/с."
#
# # result ->  25.5 1012.3 -1.2
#
# # pattern = r"-?\d+\.\d*"
# pattern = r"-?\d+\.\d*\s[а-яА-Я/]+\b"
# print(re.findall(pattern, task_text_3))


# task_text_4 = "Контакти: alice@example.org, bob.smith@mail.com."
#
# pattern = r"\b([A-Za-z0-9._-]+)@([A-Za-z.]{1,})"
#
#
# result = re.finditer(pattern, task_text_4)
#
# for match_obj in result:
#     print(f"Name: {match_obj.group(1)}\nDomen: {match_obj.group(2)}")
#     print(20 * "-")


task_text_5 = "Мій кіт любить спати. У мене є ще один Кіт. А де мій кіт?"
# Кіт -> Пес
changes_to_do = [(r"Кіт", "Пес"), (r"кіт", "пес"), (r"любить", "ненавидить")]
# pattern = r"Кіт|кіт" # r"[Кк]іт  r".іт"
# replacement = "пес"

# result = task_text_5[:]
# for pattern, replacement in changes_to_do:
#     result = re.sub(pattern, replacement, result)
#
# print(result)
# print(task_text_5)
# print(f"Original: {task_text_5}")
# print(f"After replacement: {result}")


# task_text_6 = "Це рядок      з       багатьма       пробілами."
# pattern = r"\s+"
#
# result = re.split(pattern, task_text_6)
# print(result)
# print(task_text_6.split())


