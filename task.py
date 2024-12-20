import pandas as pd
import numpy as np

# Создаем DataFrame с данными
data = {
    'Ученик': [f'Ученик {i+1}' for i in range(10)],
    'Математика': np.random.randint(60, 100, 10),
    'Физика': np.random.randint(60, 100, 10),
    'Химия': np.random.randint(60, 100, 10),
    'Биология': np.random.randint(60, 100, 10),
    'Русский язык': np.random.randint(60, 100, 10)
}

df = pd.DataFrame(data)

print(df.head())

mean_scores = df.mean(numeric_only=True)
print("Средние оценки по предметам:")
print(mean_scores)

median_scores = df.median(numeric_only=True)
print("\nМедианные оценки по предметам:")
print(median_scores)

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)

print("\nQ1 для математики:", Q1_math)
print("Q3 для математики:", Q3_math)

# Расчет IQR
IQR_math = Q3_math - Q1_math
print("IQR для математики:", IQR_math)

std_deviation = df.std(numeric_only=True)
print("\nСтандартное отклонение по предметам:")
print(std_deviation)