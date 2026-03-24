operator_name = input("Введите имя оператора: ")
pressure = input("Введите текущее значение давления (Атм): ")
with open("sensor_log.txt", "w", encoding="utf-8") as card:
    card.write(f"Имя оператора: \t\t{operator_name}\nТекущее значение давления:\t{pressure}\n")
    print(f"Данные успешно сохранены в 'sensor_log.txt'")