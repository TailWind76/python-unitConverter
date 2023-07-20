def convert_length():
    print("Выберите единицы измерения:")
    print("1. Метры")
    print("2. Километры")
    print("3. Мили")
    choice = int(input("Ваш выбор: "))

    value = float(input("Введите значение для преобразования: "))

    if choice == 1:
        print(f"{value} метров = {value * 0.001:.4f} километров")
        print(f"{value} метров = {value * 0.000621371:.4f} миль")
    elif choice == 2:
        print(f"{value} километров = {value * 1000:.4f} метров")
        print(f"{value} километров = {value * 0.621371:.4f} миль")
    elif choice == 3:
        print(f"{value} миль = {value * 1609.34:.4f} метров")
        print(f"{value} миль = {value * 1.60934:.4f} километров")
    else:
        print("Неверный выбор. Пожалуйста, выберите число от 1 до 3.")


def convert_mass():
    print("Выберите единицы измерения:")
    print("1. Килограммы")
    print("2. Фунты")
    print("3. Унции")
    choice = int(input("Ваш выбор: "))

    value = float(input("Введите значение для преобразования: "))

    if choice == 1:
        print(f"{value} килограмм = {value * 2.20462:.4f} фунтов")
        print(f"{value} килограмм = {value * 35.27396:.4f} унций")
    elif choice == 2:
        print(f"{value} фунтов = {value * 0.453592:.4f} килограмм")
        print(f"{value} фунтов = {value * 16:.4f} унций")
    elif choice == 3:
        print(f"{value} унций = {value * 0.0283495:.4f} килограмм")
        print(f"{value} унций = {value * 0.0625:.4f} фунтов")
    else:
        print("Неверный выбор. Пожалуйста, выберите число от 1 до 3.")


def convert_temperature():
    print("Выберите единицы измерения:")
    print("1. Цельсий")
    print("2. Фаренгейт")
    print("3. Кельвин")
    choice = int(input("Ваш выбор: "))

    value = float(input("Введите значение для преобразования: "))

    if choice == 1:
        fahrenheit = value * 9/5 + 32
        kelvin = value + 273.15
        print(f"{value} градусов Цельсия = {fahrenheit:.4f} градусов Фаренгейта")
        print(f"{value} градусов Цельсия = {kelvin:.4f} Кельвин")
    elif choice == 2:
        celsius = (value - 32) * 5/9
        kelvin = (value - 32) * 5/9 + 273.15
        print(f"{value} градусов Фаренгейта = {celsius:.4f} градусов Цельсия")
        print(f"{value} градусов Фаренгейта = {kelvin:.4f} Кельвин")
    elif choice == 3:
        celsius = value - 273.15
        fahrenheit = (value - 273.15) * 9/5 + 32
        print(f"{value} Кельвин = {celsius:.4f} градусов Цельсия")
        print(f"{value} Кельвин = {fahrenheit:.4f} градусов Фаренгейта")
    else:
        print("Неверный выбор. Пожалуйста, выберите число от 1 до 3.")


def main():
    print("Добро пожаловать в продвинутый конвертер единиц!")
    print("Выберите тип конверсии:")
    print("1. Длина")
    print("2. Масса")
    print("3. Температура")
    choice = int(input("Ваш выбор: "))

    if choice == 1:
        convert_length()
    elif choice == 2:
        convert_mass()
    elif choice == 3:
        convert_temperature()
    else:
        print("Неверный выбор. Пожалуйста, выберите число от 1 до 3.")


if __name__ == "__main__":
    main()
