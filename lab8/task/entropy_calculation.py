#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Расчет энтропии информационной системы SportRent
Элементарная семантическая единица: Количество заказов на аренду в день
"""

import random
import math
import json

# Параметры генерации данных
MIN_ORDERS = 50      # Минимальное количество заказов в день
MAX_ORDERS = 150     # Максимальное количество заказов в день
NUM_RECORDS = 100    # Количество записей ЭСЕ
NUM_INTERVALS = 10   # Количество интервалов для дискретизации

# Установка seed для воспроизводимости результатов
random.seed(42)

# Генерация 100 значений ЭСЕ
data = [random.randint(MIN_ORDERS, MAX_ORDERS) for _ in range(NUM_RECORDS)]

# Сортировка для удобства
data_sorted = sorted(data)

print("=" * 80)
print("РАСЧЕТ ИНФОРМАЦИОННОЙ ЭНТРОПИИ СИСТЕМЫ SportRent")
print("=" * 80)
print()
print("Элементарная семантическая единица (ЭСЕ):")
print("Количество заказов на аренду спортивного оборудования в день")
print()
print(f"Диапазон значений: от {MIN_ORDERS} до {MAX_ORDERS} заказов")
print(f"Количество записей: {NUM_RECORDS}")
print()

# Вывод первых 10 записей для отчета
print("Таблица 1 - Список элементарных семантических единиц (первые 10 записей)")
print("-" * 40)
print(f"{'№':<5} {'Наименование':<20} {'Параметр':<15}")
print("-" * 40)
for i in range(10):
    print(f"{i+1:<5} {'Заказ':<20} {data_sorted[i]:<15}")
print("-" * 40)
print()

# Сохранение всех 100 значений в файл для отчета
with open('/Users/alexgribkov/study/information-systems-design/lab8/task/data_100_records.txt', 'w', encoding='utf-8') as f:
    f.write("Полный список 100 элементарных семантических единиц:\n")
    f.write("=" * 60 + "\n\n")
    for i in range(NUM_RECORDS):
        f.write(f"{i+1:3d}. Заказ: {data_sorted[i]:3d} заказов\n")
        if (i + 1) % 20 == 0:
            f.write("\n")

# Расчет параметров для дискретизации
interval_width = (MAX_ORDERS - MIN_ORDERS) / NUM_INTERVALS
print(f"Шаг интервала: {interval_width:.1f} заказов")
print()

# Создание интервалов и подсчет частот
intervals = []
frequencies = []
interval_centers = []

for i in range(NUM_INTERVALS):
    lower_bound = MIN_ORDERS + i * interval_width
    upper_bound = MIN_ORDERS + (i + 1) * interval_width
    center = (lower_bound + upper_bound) / 2

    # Подсчет количества значений в интервале
    if i < NUM_INTERVALS - 1:
        count = sum(1 for x in data if lower_bound <= x < upper_bound)
    else:
        count = sum(1 for x in data if lower_bound <= x <= upper_bound)

    intervals.append((lower_bound, upper_bound))
    interval_centers.append(center)
    frequencies.append(count)

# Расчет вероятностей
probabilities = [freq / NUM_RECORDS for freq in frequencies]

# Вывод ряда распределения
print("Таблица 2 - Ряд распределения")
print("-" * 70)
print(f"{'№':<5} {'Интервал':<25} {'x (центр)':<15} {'n':<8} {'P(x)':<12}")
print("-" * 70)
for i in range(NUM_INTERVALS):
    interval_str = f"[{intervals[i][0]:.1f}, {intervals[i][1]:.1f})"
    print(f"{i+1:<5} {interval_str:<25} {interval_centers[i]:<15.1f} {frequencies[i]:<8} {probabilities[i]:<12.2f}")
print("-" * 70)
print()

# Проверка суммы вероятностей
prob_sum = sum(probabilities)
print(f"Сумма вероятностей: {prob_sum:.6f} (должна быть = 1.0)")
print()

# Расчет математического ожидания
expected_value = sum(center * prob for center, prob in zip(interval_centers, probabilities))
print("=" * 80)
print("РАСЧЕТ МАТЕМАТИЧЕСКОГО ОЖИДАНИЯ")
print("=" * 80)
print(f"M(x) = Σ(x_i * P(x_i))")
print(f"M(x) = {expected_value:.2f} заказов")
print()

# Расчет дисперсии
variance = sum((center - expected_value) ** 2 * prob for center, prob in zip(interval_centers, probabilities))
print("=" * 80)
print("РАСЧЕТ ДИСПЕРСИИ")
print("=" * 80)
print(f"D(x) = Σ((x_i - M(x))² * P(x_i))")
print(f"D(x) = {variance:.2f} заказов²")
print()

# Расчет среднеквадратического отклонения
std_deviation = math.sqrt(variance)
print("=" * 80)
print("РАСЧЕТ СРЕДНЕКВАДРАТИЧЕСКОГО ОТКЛОНЕНИЯ")
print("=" * 80)
print(f"σ(x) = √D(x)")
print(f"σ(x) = {std_deviation:.2f} заказов")
print()

# Расчет энтропии по формуле Шеннона
entropy = 0
for prob in probabilities:
    if prob > 0:  # log2(0) не определен
        entropy += -prob * math.log2(prob)

print("=" * 80)
print("РАСЧЕТ ЭНТРОПИИ СИСТЕМЫ (формула Шеннона)")
print("=" * 80)
print(f"H(x) = -Σ(P(x_i) * log₂(P(x_i)))")
print(f"H(x) = {entropy:.3f} бит")
print()

# Детальный расчет энтропии
print("Детальный расчет энтропии:")
print("-" * 70)
print(f"{'№':<5} {'P(x_i)':<12} {'log₂(P(x_i))':<18} {'-P(x_i)*log₂(P(x_i))':<25}")
print("-" * 70)
for i, prob in enumerate(probabilities):
    if prob > 0:
        log_prob = math.log2(prob)
        contribution = -prob * log_prob
        print(f"{i+1:<5} {prob:<12.4f} {log_prob:<18.4f} {contribution:<25.6f}")
    else:
        print(f"{i+1:<5} {prob:<12.4f} {'undefined':<18} {0.0:<25.6f}")
print("-" * 70)
print(f"{'ИТОГО:':<35} {entropy:<25.6f}")
print()

# Итоговая таблица результатов
print("=" * 80)
print("ИТОГОВАЯ ТАБЛИЦА РЕЗУЛЬТАТОВ")
print("=" * 80)
print("Таблица 3 - Параметры проектируемой ИС")
print("-" * 80)
print(f"{'Параметр':<55} {'Значение':<25}")
print("-" * 80)
print(f"{'Математическое ожидание информационного блока':<55} {expected_value:.2f} заказов")
print(f"{'Допустимый разброс значений (дисперсия)':<55} {variance:.2f} заказов²")
print(f"{'Среднеквадратическое отклонение':<55} {std_deviation:.2f} заказов")
print(f"{'Энтропия информационного наполнения':<55} {entropy:.3f} бит")
print("-" * 80)
print()

# Сохранение результатов в JSON для использования в отчете
results = {
    "ese_description": "Количество заказов на аренду спортивного оборудования в день",
    "min_value": MIN_ORDERS,
    "max_value": MAX_ORDERS,
    "num_records": NUM_RECORDS,
    "num_intervals": NUM_INTERVALS,
    "interval_width": interval_width,
    "data_first_10": data_sorted[:10],
    "intervals": [{"lower": intervals[i][0], "upper": intervals[i][1],
                   "center": interval_centers[i], "frequency": frequencies[i],
                   "probability": probabilities[i]} for i in range(NUM_INTERVALS)],
    "expected_value": expected_value,
    "variance": variance,
    "std_deviation": std_deviation,
    "entropy": entropy
}

with open('/Users/alexgribkov/study/information-systems-design/lab8/task/calculation_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Результаты сохранены в файлы:")
print("  - data_100_records.txt (все 100 записей ЭСЕ)")
print("  - calculation_results.json (результаты расчетов)")
print()
print("=" * 80)
print("РАСЧЕТ ЗАВЕРШЕН")
print("=" * 80)
