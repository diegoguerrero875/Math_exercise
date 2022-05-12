#prime
def prime(n):
    primo = True
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                primo = False

    print(n, f'is a prime? {primo}')

#fibonacci
def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range (2, n):
        c = a + b
        a = b
        b = c
        print(c)

def parnon(n):
    if n % 2 == 0:
        print(n, 'is even')
    else:
        print(n, 'is odd')


def factorial(n):
    for i in range(1, n):
        n *= i
    print(n)



def cuad(n):
    e = 0
    valor = str(n)
    for i in valor:
        e  +=int(i)**2

    print(e)


