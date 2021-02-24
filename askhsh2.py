import sys
from random import randint


def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for _ in range(2,n):
            c = a + b
            a = b
            b = c
        return b


def power(a, n, p):

    res = 1

    a = a % p

    while n > 0:

        if n % 2:
            res = (res * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p
            n = n // 2
    return res % p


def isPrime(n, k):
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(k):
            a = randint(2, n - 2)

            # Fermat's little theorem
            if power(a, n - 1, n) != 1:
                return False
    return True


if __name__ == '__main__':

    try:
        n = int(input("Give n: "))
    except Exception as e:
        sys.exit(f"Error: {e} \nPlease give integer!")

    fib = fibonacci(n)

    prime = isPrime(fib,20)

    if prime:
        print(f"{fib} is a prime")
    else:
        print(f"{fib} is not a prime")
