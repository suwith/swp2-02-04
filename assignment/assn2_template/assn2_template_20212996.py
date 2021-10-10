import time
import random

#선형탐색
def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1

#이진탐색 재귀함수로 구현하기(과제)
def recbinsearch(L, l, u, target):
    #L:탐색대상 리스트 l: lower u: upper target: key
    if(l<u):
        m = int((l + u) // 2)
        if L[m] == target:
            return m
        elif L[m] < target:
            return recbinsearch(L, m+1, u, target)
        else:
            return recbinsearch(L, l, m-1, target)
    else: return -1

#탐색대상 리스트 랜덤 생성
numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]

numbers = sorted(numbers)

#타겟대상 리스트 랜덤 생성
numoftargets = int(input("Enter the number of targets: "))
targets = []
for i in range(numoftargets):
    targets += [random.randint(0, 999999)]


ts = time.time()

# binary search - recursive
cnt = 0
idx = -1
for target in targets:
    idx = recbinsearch(numbers, 0, len(numbers), target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("recbinsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))

ts = time.time()

# sequential search
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("seqsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))
