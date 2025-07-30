# a = "123"
#
# print(a - 123)

# SyntaxError
# a = "123"
# if a = str(123):
#     print(a)

# TypeError
# print(6 / "2")
# len(123)

# ValueError
# int("abc")
# print(-1 ** 0.5)
# import math
#
# print(math.sqrt(-1))

# NameError
# print(a)

# IndexError
# a = [1, 2, 3]
# print(a[3])

# KeyError
# print(45 / 0)
# FileNotFoundError
# FileExistsError()

# try:
#     pass
#     # Код, який може допустити помилку
# except ZeroDivisionError:
#     pass
#     # /0 ERROR
# except ValueError as e:
#     pass
# except (IndexError, KeyError):
#     pass
# except Exception as error:
#     # Обробляти помилку
#     pass
# else:
#     # Якщо не було помилок у try
#     pass
# finally:
#     # Блок який виконується завжди
#     pass
#
# def save_divide(numerator:int|float, denominator:int|float):
#     try:
#         result = numerator / denominator
#         print(f"{numerator} / {denominator} = {result}")
#     except ZeroDivisionError as error:
#         print(error)
#         print("Zero division")
#     except TypeError as error:
#         print("Incorrect type")
#         print(error)
#     print("Block after division")
#
# save_divide(10, 2)
# print("-" * 30)
# save_divide(23, 0)
# print("-" * 30)
# save_divide("123" , 8)
#
# print("123" - 12)


# class InvalidInputError(Exception):
#     """Exception in invalid input type"""
#     def __init__(self, message="Incorrect dtype of object"):
#         self.message = message
#         super().__init__(self.message)
#
# def get_user_by_id(id):
#     if id < 0:
#         raise InvalidInputError("ID is negative number")
#     return {"user_id": id, "user_name": "Test"}
#
# try:
#     print(get_user_by_id(12))
#     print(get_user_by_id(-13))
# except InvalidInputError as e:
#     print(e)


# import random
#
# class InvalidUserDataError(Exception):
#     """Виняток, що виникає при некоректних даних користувача."""
#     def __init__(self, field, value, message="Некоректні дані користувача."):
#         self.field = field
#         self.value = value
#         self.message = f"{message} Поле: '{field}', Значення: '{value}'"
#         super().__init__(self.message)
#
# class DatabaseConnectionError(Exception):
#     """Виняток, що виникає при проблемах з підключенням до БД."""
#     def __init__(self, db_name, message="Помилка підключення до бази даних."):
#         self.db_name = db_name
#         self.message = f"{message} БД: '{db_name}'"
#         super().__init__(self.message)
#
#
# def create_new_user(username, password, email):
#     if not username or len(username) < 3:
#         raise InvalidUserDataError("username", username, "Ім'я користувача має бути не менше 3 символів.")
#     if not password or len(password) < 8:
#         raise InvalidUserDataError("password", "********","Пароль має бути не менше 8 символів.")
#     if "@" not in email:
#         raise InvalidUserDataError("email", email,"Некоректний формат email.")
#     # Імітація збереження в БД (може викликати DatabaseConnectionError)
#     if random.random() < 0.1: # 10% шанс на помилку БД
#         raise DatabaseConnectionError("main_db")
#     print(f"Користувач '{username}' успішно створений.")
#     return {"username": username, "email": email}
#
# for i in range(10):
#     username = f"test_{i}"
#     password = "pass123password"
#     email = "test@mail.com"
#
#     if i == 3:
#         username = "pp"
#     elif i == 5:
#         password = "pass"
#     elif i == 7:
#         email = "test_mail.com"
#
#     try:
#         new_user = create_new_user(username, password,  email)
#     except InvalidUserDataError as error:
#         print(f"Валідація користувача не успішна. Помилка: {error}")
#         print(f"Поле: {error.field}, Значення: {error.value}")
#     except DatabaseConnectionError as error:
#         print(f"Помилка підключення до бази данних: {error.db_name}")
#     else:
#         print(new_user)


import json
import random

def parse_json_request(json_sting):
    try:
        data = json.loads(json_sting)
        return data
    except json.JSONDecodeError as e:
        raise ValueError(f"Incorrect format of json_string: {e}")

def process_order_requests(reqeust_body):
    try:
        data = parse_json_request(reqeust_body)

        product_id = data.get("id")
        quantity = data.get("quantity", 0)


        if not isinstance(product_id, int) or product_id <= 0:
            raise ValueError("Product id must be greater than 0.")
        if not isinstance(quantity, int) or quantity <= 0 :
            raise ValueError("Quantity must be greater than 0.")


        print(f"Order processed: ID: {product_id}, Quantity: {quantity}")
        return {"status": "success", "order_id": random.randint(100, 1000)}

    except ValueError as e:
        return {"status": "error", "message": e}
    except Exception as e:
        print(e)
        return {"status": "error", "message": "Processing error"}


order = {"id": "567", "quantity": 4}
response = process_order_requests(json.dumps(order))
print(response)
