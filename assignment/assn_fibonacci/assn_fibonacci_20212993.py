import time

#반복
def Interfibo(n):
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b

#재귀
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break

    ts = time.time()
    fibonumber = Interfibo(nbr)
    ts = time.time() - ts
    print("InterFibo(%d) = %d, time %.6f" % (nbr, fibonumber, ts)
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d) = %d, time %.6f" % (nbr, fibonumber, ts))
