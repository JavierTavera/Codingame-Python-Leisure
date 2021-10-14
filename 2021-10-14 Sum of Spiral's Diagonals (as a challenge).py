n2 = n = int(input())
sum = 0
actual_number = 1
while(n2 > 1):
    for i in range(4):
        sum += actual_number # Adding the corners
        actual_number += n2 - 1 # Calculating the corners
    n2 -= 2
if n2 == 1: sum += pow(n,2)
print(sum)
