def add(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Parameters must be numeric")
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("divoder must != 0.")
    return a / b

def is_polindrome(text:str):
    processed_text = "".join(list(filter(str.isalnum, text))).lower()
    return processed_text == processed_text[::-1]

def calculate_discount(price, discount_percentage):
    """
    Обчислює ціну після застосування знижки.
    Повертає ціну зі знижкою.
    Викликає ValueError, якщо discount_percentage не в діапазоні [0, 100].
    """
    if not (0 <= discount_percentage <= 100):
        raise ValueError("Відсоток знижки має бути від 0 до 100.")
    return price * (1 - discount_percentage / 100)

def reverse_list(input_list):
    """Повертає новий список з елементами у зворотному порядку."""
    if not isinstance(input_list, (list, tuple)):
        raise TypeError("Input is not list or tuple.")
    return input_list[::-1]

def find_max_value(numbers:list):
    """Повертає максимальне значення зі списку чисел. Повертає None для порожнього списку."""
    if not numbers:
        return None
    return max(numbers)

def format_user_name(first_name, last_name):
    """Форматує ім'я користувача як 'Прізвище, Ім'я'."""
    return f"{last_name}, {first_name}"