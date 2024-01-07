def FindingMaxOfList(spisok):
    return max(spisok)

cnt = int(input("Введите количество элементов массива: "))
spisok = input("Введите элементы массива: ").split()[:cnt]
print("Максимум: " + FindingMaxOfList(spisok))
