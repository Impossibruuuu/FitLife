# Проект FitLife - MVP версия 1.1
WATER_PER_KG = 30
ML_PER_L = 1000
BORDER_WIDTH = 50
BMI_DESCRIPTIONS = {
    "Недостаточный вес": "Вес ниже нормы, возможен дефицит питательных"
    " веществ",
    "Норма": "Здоровый вес, соответствующий росту",
    "Избыточный вес": "Вес выше нормы, рекомендуется скорректировать питание"
    " и активность",
    "Ожирение": "Значительное превышение нормы веса, рекомендуется "
    "консультация врача"
}

# 1. Знакомство
while True:
    user_name = input("Введите ваше имя: ").strip().title()

    if user_name == "":
        print("Имя не может быть пустым. Попробуйте ещё раз")
        continue
    break

print(f"Здравствуйте, {user_name}!")

while True:
    age_input = input("Введите ваш возраст: ").strip()

    if age_input == "":
        print("Возраст не может быть пустым. Попробуйте ещё раз")
        continue
    try:
        user_age = int(age_input)
        if user_age <= 0:
            print("Возраст должен быть положительным числом")
            continue
        break
    except ValueError:
        print("Введите корректное число")


# 2. Сбор данных
while True:
    weight_input = input("Введите ваш вес в кг (например, 70.45): ")

    if weight_input == "":
        print("Вес не может быть пустым. Попробуйте ещё раз")
        continue
    try:
        user_weight = float(weight_input)
        if user_weight <= 0:
            print("Вес должен быть положительным числом")
            continue
        break
    except ValueError:
        print("Введите корректное число")

while True:
    height_input = input("Введите ваш рост в метрах (например, 1.75): ")

    if height_input == "":
        print("Рост не может быть пустым. Попробуйте ещё раз")
        continue
    try:
        user_height = float(height_input)
        if user_height <= 0:
            print("Вес должен быть положительным числом")
            continue
        break
    except ValueError:
        print("Введите корректное число")

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = round(user_weight / (user_height**2), 1)

if bmi < 18.5:
    bmi_category = "Недостаточный вес"
elif bmi < 25:
    bmi_category = "Норма"
elif bmi < 30:
    bmi_category = "Избыточный вес"
elif bmi >= 30:
    bmi_category = "Ожирение"

# Подсчет воды: вес * 30 мл
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_PER_L
water_needed = round(water_l, 2)

# 4. Вывод красивого результата
print()
print("=" * BORDER_WIDTH)
print()
print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi} ({bmi_category})")
print(f"Рекомендуемая норма воды: {water_needed} л. в день")
print()
print("=" * BORDER_WIDTH)
print()
print(f"Пояснение значения индекса {bmi} ({bmi_category}):")
print(BMI_DESCRIPTIONS[bmi_category])
print()
print("=" * BORDER_WIDTH)
print()
print("Расчет окончен. Будьте здоровы!")
