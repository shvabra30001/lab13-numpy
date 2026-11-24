import numpy as np

# Задание 1. Первый одномерный массив и его атрибуты
print("--- Задание 1 ---")
numbers = list((4, 8, 15, 16, 23))
arr = np.array(numbers)
print("Тип объекта:", type(arr))
print("Форма (shape):", arr.shape)
print("Размер (size):", arr.size)
print("Массив:", arr)

# Задание 2. Векторная операция: перевод температур из Цельсия в Фаренгейты
print("\n--- Задание 2 ---")
celsius = np.array(list((0, 12, 24, 30, 36)))
fahrenheit = celsius * 9 / 5 + 32
print("Цельсии:   ", celsius)
print("Фаренгейты:", fahrenheit)

# Задание 3. Статистика времени выполнения задач ИИ-модели (7 значений)
print("\n--- Задание 3 ---")
times = np.array(list((115, 92, 84, 108, 79, 134, 96)))
print("Среднее время:     ", np.mean(times))
print("Максимум:          ", np.max(times))
print("Минимум:           ", np.min(times))
print("Станд. отклонение: ", np.std(times))
print("Сумма:             ", np.sum(times))

# Задание 4. Двумерный массив (матрица весов 3x3) и срезы
print("\n--- Задание 4 ---")
weights = np.array(list((
    list((0.1, 0.2, 0.3)),
    list((0.4, 0.5, 0.6)),
    list((0.7, 0.8, 0.9))
)))
print("Матрица:\n", weights)
print("Форма матрицы:     ", weights.shape)
print("Первая строка:     ", weights[0, :])
print("Последний столбец: ", weights[:, -1])
print("Элемент:    ", weights[1, 2])

# Задание 5. Фильтрация через булеву маску (числа больше 50)
print("\n--- Задание 5 ---")
np.random.seed(42)
randoms = np.random.randint(1, 101, size=100)
mask = randoms > 50
big = randoms[mask]
print("Всего чисел:      ", randoms.size)
print("Чисел больше 50:  ", big.size)
print("Отобранные числа: ", big)

# Задание 6. Мини-кейс: оценки 5 студентов по 3 предметам (оси axis)
print("\n--- Задание 6 ---")
grades = np.array(list((
    list((5, 4, 3)),
    list((4, 4, 5)),
    list((3, 5, 5)),
    list((4, 3, 4)),
    list((5, 5, 4))
)))
by_student = grades.mean(axis=1)  # среднее по строкам (для каждого студента)
by_subject = grades.mean(axis=0)  # среднее по столбцам (по каждому предмету)
print("Средний балл каждого студента:", by_student)
print("Средний балл по предметам:    ", by_subject)
