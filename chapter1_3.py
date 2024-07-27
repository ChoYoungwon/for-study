import random

def gcd(a, b):
    c, d = a, b
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    c = gcd(a, b)
    result = c * (a//c)*(b//c)
    print(f'최대 공약수 : {c} / 최소 공배수 : {c} * {a//c} * {b//c}')
    print(f'{a}과 {b}의 최소 공배수 = ', result)
    print('\n')

for _ in range(5):
    lcm(random.randrange(60)+1, random.randrange(60)+1)