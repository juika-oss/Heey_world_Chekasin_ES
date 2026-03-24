f = open("inventory.txt", "w", encoding="utf-8")
reagent_name = input()
quantity = int(input())

print(f'Реактив {reagent_name} поступил на склад в количестве {quantity} шт.', file=f)
f.close()