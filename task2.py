from collections import deque

def is_palindrome(s):
    # Переведення рядка в нижній регістр і видалення пробілів
    s = s.replace(" ", "").lower()

    # Додавання символів рядка до двосторонньої черги
    dq = deque(s)

    # Порівняння символів з обох кінців черги
    while len(dq) > 1:
        left = dq.popleft()  # Видалення символа з лівого кінця
        right = dq.pop()  # Видалення символа з правого кінця

        # Перевірка на рівність
        if left != right:
            return False

    return True

# Тестування функції
test_strings = ["A man a plan a canal Panama", "No lemon no melon", "Palindrome", "Was it a car or a cat I saw"]

for ts in test_strings:
    print(f"'{ts}' - паліндром: {is_palindrome(ts)}")