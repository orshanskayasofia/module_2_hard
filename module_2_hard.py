import random

def challenge(n):
    number = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                number += str(i) + str(j)
    return  f'{n} - {number}'
numbers = (3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)
n = random.choice(numbers)

result = challenge(n)
print(result)








