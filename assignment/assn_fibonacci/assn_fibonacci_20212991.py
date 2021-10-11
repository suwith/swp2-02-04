import time


def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

def iterfibo(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a



while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("Iterfibo(%d) = %d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d) = %d, time %.6f" %(nbr, fibonumber, ts))
