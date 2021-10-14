import time

#반복적 피보나치
def iterfibo(n):
    lst = [0, 1]
    for i in range(1, n):
        lst.insert(i+1, lst[i-1] + lst[i])
    return lst[n]

#재귀적 피보나치
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break

    #반복적 피보나치
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))

   #재귀적 피보나치
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))

