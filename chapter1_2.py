import random

def gcd(a, b):
    c, d = a, b
    while b != 0:
        r = a % b
        a = b
        b = r
        print(f'gcd({a}, {b})')
    print(f'{c}과 {d}의 최대 공약수 = ', a)
    print('\n')
    return

for _ in range(5):
    gcd(random.randrange(60)+1, random.randrange(60)+1)