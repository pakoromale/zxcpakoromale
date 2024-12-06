import tkinter as tk
import tkinter.filedialog as filedialog
import random
import statistics
import os
import pathlib

# Функция для приветствия пользователя
def greet_user():
    """
    Функция получает имя пользователя из поля ввода и отображает сообщение с приветствием.
    Если имя введено, обновляется текст на метке с приветствием.
    """
    name = name_entry.get()  # Получаем значение из поля ввода имени
    if name:  # Если имя введено
        name_label.config(text=f"Привет, {name}!")  # Обновляем метку с приветствием

# Функция для выполнения математических операций
def calculate_math():
    """
    Функция выполняет несколько математических операций (сложение, вычитание, умножение, деление)
    с двумя числами, введёнными пользователем. Результат отображается на метке.
    В случае ошибки (нечисловое значение или деление на 0) выводится соответствующее сообщение.
    """
    try:
        # Преобразуем значения из полей ввода в числа с плавающей запятой
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        results = {
            "Сумма": num1 + num2,
            "Разность": num1 - num2,
            "Произведение": num1 * num2,
            "Частное": num1 / num2 if num2 != 0 else "Деление на 0 невозможно",  # Обработка деления на 0
        }
        # Формируем строку с результатами
        result_text = "\n".join(f"{k}: {v}" for k, v in results.items())
        result_label.config(text=result_text)  # Отображаем результаты на метке
    except ValueError:
        result_label.config(text="Ошибка: Введите числа!")  # Ошибка при вводе некорректных данных
    except ZeroDivisionError:
        result_label.config(text="Ошибка: Деление на 0 невозможно!")  # Ошибка деления на 0

# Функция для выбора директории
def select_directory():
    """
    Функция вызывает диалоговое окно для выбора директории.
    Выбранный путь отображается в соответствующем поле ввода.
    """
    directory = filedialog.askdirectory()  # Открываем диалог выбора директории
    if directory:
        directory_entry.delete(0, tk.END)  # Очищаем поле ввода
        directory_entry.insert(0, directory)  # Вставляем выбранный путь

# Функция для генерации файлов с случайными числами
def generate_files():
    """
    Функция генерирует 3 текстовых файла с 10 случайными числами от 1 до 100 в каждом.
    Файлы сохраняются в указанной директории.
    Если директория не выбрана, выводится ошибка.
    """
    target_directory = directory_entry.get()  # Получаем путь из поля ввода
    if not target_directory:
        result_label.config(text="Ошибка: Выберите директорию!")  # Ошибка, если путь не указан
        return

    try:
        os.makedirs(target_directory, exist_ok=True)  # Создаём директорию, если она не существует
        for i in range(1, 4):
            filename = os.path.join(target_directory, f"numbers_{i}.txt")
            # Генерация случайных чисел
            numbers = [str(random.randint(1, 100)) for _ in range(10)]
            with open(filename, "w") as f:
                f.write("\n".join(numbers))  # Записываем числа в файл
        result_label.config(text="Файлы успешно созданы!")  # Успешное завершение
    except Exception as e:
        result_label.config(text="Ошибка: при создании файлов!")  # Ошибка при создании файлов

# Функция для вычисления среднего значения чисел из файла
def calculate_average():
    """
    Функция вычисляет среднее арифметическое чисел из выбранного текстового файла.
    Если файл пуст или данные некорректны, выводится ошибка.
    """
    filename = file_entry.get()  # Получаем имя файла из поля ввода
    if not filename:
        result_label.config(text="Ошибка: Выберите файл!")  # Ошибка, если файл не выбран
        return
    try:
        with open(filename, "r") as f:
            # Чтение чисел из файла
            numbers = [int(line.strip()) for line in f if line.strip().isdigit()]
            if numbers:
                avg = statistics.mean(numbers)  # Вычисление среднего
                result_label.config(text=f"Среднее: {avg}")  # Отображение результата
            else:
                result_label.config(text="Ошибка: Файл пустой или содержит некорректные данные.")
    except FileNotFoundError:
        result_label.config(text=f"Ошибка: Файл {filename} не найден.")  # Ошибка, если файл не найден
    except ValueError:
        result_label.config(text=f"Ошибка: Ошибка обработки данных в файле {filename}.")  # Ошибка обработки данных
    except Exception as e:
        result_label.config(text=f"Ошибка: {e}")  # Общая ошибка

# Функция для выбора файла через диалоговое окно
def browse_file():
    """
    Функция вызывает диалоговое окно для выбора текстового файла.
    Путь к выбранному файлу отображается в соответствующем поле ввода.
    """
    filepath = filedialog.askopenfilename(
        defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )  # Открытие диалога выбора файла
    if filepath:
        file_entry.delete(0, tk.END)  # Очищаем поле ввода
        file_entry.insert(0, filepath)  # Вставляем путь к выбранному файлу

# Создание главного окна
window = tk.Tk()
window.title("Мое приложение")

# Создание виджетов
directory_label = tk.Label(window, text="Выберите директорию:")
directory_entry = tk.Entry(window, width=40)
select_directory_button = tk.Button(window, text="Выбрать", command=select_directory)
generate_button = tk.Button(window, text="Создать файлы", command=generate_files)

name_label = tk.Label(window, text="Имя:")
name_entry = tk.Entry(window)
greet_button = tk.Button(window, text="Привет!", command=greet_user)

num1_label = tk.Label(window, text="Число 1:")
num1_entry = tk.Entry(window)
num2_label = tk.Label(window, text="Число 2:")
num2_entry = tk.Entry(window)
calculate_button = tk.Button(window, text="Вычислить", command=calculate_math)
result_label = tk.Label(window, text="")

file_label = tk.Label(window, text="Выберите файл:")
file_entry = tk.Entry(window)
browse_button = tk.Button(window, text="Обзор...", command=browse_file)
calculate_avg_button = tk.Button(window, text="Вычислить среднее", command=calculate_average)

# Размещение виджетов в окне с использованием сетки
directory_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)
directory_entry.grid(row=4, column=2, columnspan=2, padx=5, pady=5)
select_directory_button.grid(row=4, column=5, padx=5, pady=5)
generate_button.grid(row=5, column=3, columnspan=4, pady=10)

name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry.grid(row=0, column=1, padx=5, pady=5)
greet_button.grid(row=0, column=2, padx=5, pady=5)

num1_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
num1_entry.grid(row=1, column=1, padx=5, pady=5)
num2_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
num2_entry.grid(row=2, column=1, padx=5, pady=5)
calculate_button.grid(row=2, column=2, padx=5, pady=5)
result_label.grid(row=3, column=0, columnspan=3, pady=5)

file_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
file_entry.grid(row=5, column=1, padx=5, pady=5)
browse_button.grid(row=5, column=2, padx=5, pady=5)
calculate_avg_button.grid(row=6, column=0, columnspan=3, pady=10)

result_label.grid(row=7, column=0, columnspan=3, pady=10)

# Запуск главного цикла приложения
window.mainloop()
