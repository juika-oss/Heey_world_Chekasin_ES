all_capsules = float(input("Введите общее количество произведенных капсул: "))
package_capsules = float(input("Введите количество капсул в одной упаковке: "))
packages = all_capsules // package_capsules
capsules = all_capsules % package_capsules
print("---Отчет фасовочного цеха---" )
print(f"Полных упаковок: \t{packages}\nОстаток капсул: \t{capsules}")
