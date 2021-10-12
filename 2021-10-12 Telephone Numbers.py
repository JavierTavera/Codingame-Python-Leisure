n = int(input())
arbol = set()
max_letters = 0
for i in range(n):
    telephone = input()
    arbol.add(telephone)
    if len(telephone) > max_letters: max_letters = len(telephone)

conteo = 0
previous_num = {}
for i in range(20):
    previous_num[i] = []

for conteo_1 in range(max_letters):
    for item in arbol:
        if len(item) > conteo_1 and not item[:conteo_1 + 1] in previous_num[conteo_1]:
            previous_num[conteo_1] = previous_num[conteo_1] + [item[:conteo_1 + 1]]
            conteo += 1

print(conteo)
