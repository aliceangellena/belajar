x = int(input("Masukkan batas Fibonacci: "))
n = 0

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if x <= 0:
    print("Batas tidak valid!")
else:
    while n < x:
        print(fibonacci(n))
        n += 1
