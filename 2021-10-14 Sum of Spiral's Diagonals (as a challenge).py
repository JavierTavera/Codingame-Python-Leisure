n = int(input())
n2 = n
sum = 0
nro_actual = 1

while(n2 > 1):
    for i in range(4):
        sum += nro_actual # Adding the corners
        nro_actual += n2 - 1 # Calculating the corners
    n2 -= 2

if n2 == 1:
    sum += pow(n,2)

print(sum)
