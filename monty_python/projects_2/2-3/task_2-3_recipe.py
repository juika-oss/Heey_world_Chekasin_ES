medium_name = input("Название питательноей среды: ")
agar = input("Концентрация агара (%): ")
temp = input("Температура стерилизации:")
with open("recipe.txt", "w", encoding="utf-8") as card:
    card.write(f"Название питательноей среды: {medium_name}\nКонцентрация агара (%):{agar}\nТемпература стерилизации(°C): {temp}\n")
    print(f"\nФайл 'recipe.txt' успешно сформирован!")