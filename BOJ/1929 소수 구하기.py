import math

m, n = map(int, input().split())

isPrime = [1 for _ in range(n+1)]
isPrime[0], isPrime[1] = 0, 0

length = int(math.sqrt(n))

for i in range(2, length+1):
  if isPrime[i]:
    for j in range(i*2, n+1, i):
      isPrime[j] = 0

for i in range(m, n+1):
  if isPrime[i]:
    print(i)
