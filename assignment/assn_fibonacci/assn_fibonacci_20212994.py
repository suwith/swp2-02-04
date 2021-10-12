import time

# 반복 알고리즘을 이용한 피보나치 수열
def iterfibo(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a+b
    return a

# 재귀 알고리즘을 이용한 피보나치 수열
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

while True:
    nbr = int(input("Enter a number : "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d) = %d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d) = %d, time %.6f" % (nbr, fibonumber, ts))
