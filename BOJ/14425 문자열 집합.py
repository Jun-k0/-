# set을 사용

n, m = map(int,input().split())
mySet = set()
ans = 0

for _ in range(n):
  mySet.add(input())

for _ in range(m):
  test = input()
  if test in mySet:
    ans += 1

print(ans)
