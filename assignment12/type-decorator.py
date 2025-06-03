# декоратор с параметром  type_of_output
def type_decorator(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator

# Функция возвращает int, декорирована преобразованием в str
@type_decorator(str)
def return_int():
    return 5

#  Функция возвращает строку, декорирована преобразованием в int
@type_decorator(int)
def return_string():
    return "not a number"

#  Основной код
if __name__ == "__main__":
    y = return_int()
    print(type(y).__name__)  # Ожидается: str

    try:
        y = return_string()  # Попытка преобразовать "not a number" в int
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer!")  # Это и должно произойти