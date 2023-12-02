# Berilgan massiv
massiv = [3, 4, 2, 5, 4, 2, 7, 3, 8, 1, 2, 4, 6, 7, 6, 1, 8, 1, 1, 3, 4, 5]

# Tartiblash
n = len(massiv)
for i in range(n):
    for j in range(0, n-i-1):
        if massiv[j] > massiv[j+1]:
            massiv[j], massiv[j+1] = massiv[j+1], massiv[j]

# Necha marta takrorlanganligini hisoblash
takrorlanishlar = {}
for element in massiv:
    if element in takrorlanishlar:
        takrorlanishlar[element] += 1
    else:
        takrorlanishlar[element] = 1

# Natijani chiqarish
for key, value in takrorlanishlar.items():
    print(f"{key} - {value} marta")
