with open("nucl_count.txt", "w", encoding="utf-8") as ATGC:
    ATGC.write("=== Анализ последовательности ДНК ===\n")

    DNA = input("Введите последовательность ДНК: ").upper()

    count_A = DNA.count("A")
    count_C = DNA.count("C")
    count_G = DNA.count("G")
    count_T = DNA.count("T")

    count_all = count_A + count_C + count_G + count_T
    one_procent = 100 / count_all

    ATGC.write(f"\nПоследовательность в верхнем регистре: {DNA}\n\n")
    ATGC.write("Подсчёт нуклеотидов:\n")
    ATGC.write(f"A: {count_A}\n")
    ATGC.write(f"T: {count_C}\n")
    ATGC.write(f"G: {count_G}\n")
    ATGC.write(f"C: {count_T}\n")
    ATGC.write(f"\nОбщая длина: {count_all}\n")
    ATGC.write("\nПроцентное содержание нуклеотидов:\n")
    ATGC.write(f"A (%): {one_procent * count_A:.3f}\n")
    ATGC.write(f"T (%): {one_procent * count_C:.3f}\n")
    ATGC.write(f"G (%): {one_procent * count_G:.3f}\n")
    ATGC.write(f"C (%): {one_procent * count_T:.3f}")
