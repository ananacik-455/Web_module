import functools
import time
import datetime
import random
import collections

# Створіть декоратор `cache_results`, який кешує результати виконання функції.
# Якщо функція викликається з тими ж аргументами, поверніть кешований результат,
# не виконуючи функцію повторно.
# Використовуйте словник для зберігання кешу.


# Ваш код декоратора cache_results тут:
def cache_results(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Логіка кешування
        return result
    return wrapper


@cache_results
def fetch_data_from_db(item_id):
    """Імітує отримання даних з бази даних."""
    print(f"Отримання даних для item_id={item_id} з БД...")
    time.sleep(0.5) # Імітація затримки
    return {"id": item_id, "value": random.randint(1, 100)}

print("Тестування Завдання 2:")
print(fetch_data_from_db(1))
print(fetch_data_from_db(2))
print(fetch_data_from_db(1)) # Має бути взято з кешу
print(fetch_data_from_db(3))
print(fetch_data_from_db(2)) # Має бути взято з кешу




#  Завдання 3: Декоратор для обмеження кількості викликів (Rate Limiting)
# Створіть декоратор `rate_limit`, який обмежує кількість викликів функції
# до `max_calls` протягом `period_seconds`.
# Якщо ліміт перевищено, виведіть повідомлення та не виконуйте функцію.
# Це корисно для захисту API-ендпоінтів від надмірного використання.


# Ваш код декоратора rate_limit тут:
def rate_limit(max_calls, period_seconds):
    calls = collections.deque() # Використовуйте deque для зберігання часу викликів
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Логіка обмеження
             return func(*args, **kwargs)
        return wrapper
    return decorator


@rate_limit(max_calls=3, period_seconds=5)
def send_notification(user_id, message):
    """Імітує відправлення сповіщення користувачу."""
    print(f"Надсилаю сповіщення користувачу {user_id}: '{message}'")
    return True

print("Тестування Завдання 3:")
for i in range(5):
    send_notification(f"user_{i}", f"Привіт {i}!")
    time.sleep(1) # Затримка для перевірки ліміту




# Завдання 4: Декоратор для перетворення результату (Response Transformer)
# Створіть декоратор `json_response`, який перетворює результат функції
# (припускається, що це словник) на JSON-рядок.
# Це імітує поведінку веб-фреймворків, які автоматично серіалізують відповіді.


import json

# Ваш код декоратора json_response тут:
def json_response(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Логіка перетворення
        return json_string
    return wrapper


@json_response
def get_user_data(user_id):
    """Повертає дані користувача у вигляді словника."""
    return {"id": user_id, "name": "Тестовий Користувач", "email": f"user{user_id}@example.com"}

@json_response
def get_product_list():
    """Повертає список продуктів."""
    return [{"id": 1, "name": "Ноутбук"}, {"id": 2, "name": "Мишка"}]

print("Тестування Завдання 4:")
user_data_json = get_user_data(1)
print(f"Дані користувача (JSON): {user_data_json}")
print(f"Тип даних: {type(user_data_json)}")

product_list_json = get_product_list()
print(f"Список продуктів (JSON): {product_list_json}")




# Завдання 5: Декоратор для перенаправлення (Redirect Decorator)
# Створіть декоратор `redirect_if_unauthenticated`, який імітує перенаправлення
# на сторінку входу, якщо користувач не аутентифікований.
# Це типова поведінка у веб-додатках.

# Імітація стану аутентифікації
is_authenticated = False

# Ваш код декоратора redirect_if_unauthenticated тут:
def redirect_if_unauthenticated(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Логіка перевірки аутентифікації та перенаправлення
        return func(*args, **kwargs)
    return wrapper


@redirect_if_unauthenticated
def dashboard_page():
    """Сторінка панелі керування, доступна лише аутентифікованим користувачам."""
    return "Ви на сторінці панелі керування!"

@redirect_if_unauthenticated
def settings_page():
    """Сторінка налаштувань."""
    return "Сторінка налаштувань."

print("Тестування Завдання 5:")
print(dashboard_page()) # Має бути "Перенаправлення на сторінку входу..."
print(settings_page())  # Має бути "Перенаправлення на сторінку входу..."

is_authenticated = True # Імітуємо аутентифікацію
print("\n(Після аутентифікації)")
print(dashboard_page()) # Має бути "Ви на сторінці панелі керування!"
print(settings_page())  # Має бути "Сторінка налаштувань."

