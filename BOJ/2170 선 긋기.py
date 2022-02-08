n = int(input())
linear = []
ans = []

for _ in range(n):
  s, e = map(int, input().split())
  linear.append((s,e))

linear.sort(key=lambda x:x[0])
nowStart, nowEnd = linear[0]

for start, end in linear:
  if start <= nowEnd:
    if end >= nowEnd:
      nowEnd = end
  elif start > nowEnd:
    ans.append((nowStart, nowEnd))
    nowStart = start
    nowEnd = end

ans.append((nowStart, nowEnd))

sum = 0
for start, end in ans:
  sum += end - start

# print(ans)
print(sum)
