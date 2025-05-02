import pandas as pd
import numpy as np



# Задаем список фамилий и имен учеников
student_names = [
    "Иванов Иван",
    "Петрова Мария",
    "Сидоров Алексей",
    "Смирнова Дарья",
    "Кузнецов Михаил",
    "Васильева Анна",
    "Попов Дмитрий",
    "Соколова Елена",
    "Михайлов Сергей",
    "Новикова Ольга"
]

# Задаем названия предметов
subjects = ['Математика', 'Физика', 'Химия', 'История', 'Литература']

# 1.3 Генерируем случайные оценки (от 3 до 5)
# Устанавливаем seed для воспроизводимости результатов
np.random.seed(42)
num_students = len(student_names)
num_subjects = len(subjects)
grades = np.random.randint(3, 6, size=(num_students, num_subjects))

#  Создаем DataFrame
df = pd.DataFrame(grades, index=student_names, columns=subjects)

# Присваиваем имя индексу (столбцу с именами учеников)
df.index.name = "Имя Фамилия"

print("--- Анализ данных учеников ---")

#  Вывод первых строк DataFrame ---
print("\nПервые 5 строк DataFrame:")
print(df.head())
print("-" * 30) # Разделитель для читаемости

#  Вычисление средней оценки по каждому предмету ---
mean_grades = df.mean()
print("\nСредняя оценка по каждому предмету:")
print(mean_grades)
print("-" * 30)

#  Вычисление медианной оценки по каждому предмету ---
median_grades = df.median()
print("\nМедианная оценка по каждому предмету:")
print(median_grades)
print("-" * 30)

# Вычисление Q1, Q3 и IQR для оценок по математике ---
print("\nСтатистика для оценок по Математике:")
try:
    # Проверяем, есть ли столбец 'Математика'
    if 'Математика' in df.columns:
        Q1_math = df['Математика'].quantile(0.25)
        Q3_math = df['Математика'].quantile(0.75)
        IQR_math = Q3_math - Q1_math

        print(f"Q1 (Первый квартиль) по Математике: {Q1_math}")
        print(f"Q3 (Третий квартиль) по Математике: {Q3_math}")
        print(f"IQR (Межквартильный размах) по Математике: {IQR_math}")
    else:
        print("Столбец 'Математика' не найден в DataFrame.")
except Exception as e:
    print(f"Ошибка при расчете статистики по Математике: {e}")
print("-" * 30)

# Вычисление стандартного отклонения оценок по каждому предмету ---
std_dev_grades = df.std()
print("\nСтандартное отклонение оценок по каждому предмету:")
print(std_dev_grades)
print("-" * 30)

#  Дополнительно: Общая статистика ---
print("\nОбщая  статистика:")
print(df.describe())
print("-" * 30)

# --- Шаг 7: Сохранение DataFrame в CSV файл ---
csv_filename = 'student_grades.csv'
try:
    # Используем encoding='utf-8-sig' для лучшей совместимости с Excel на Windows
    df.to_csv(csv_filename, encoding='utf-8-sig')
    print(f"\nDataFrame успешно сохранен в файл: {csv_filename}")
except Exception as e:
    print(f"\nОшибка при сохранении файла '{csv_filename}': {e}")

