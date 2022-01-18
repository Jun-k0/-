s = input()

cntNumZero = 0
cntNumOne = 0

for num in range(1, len(s)):
  if s[num - 1] != s[num]:
    if s[num] == "0":
      cntNumZero += 1
    if s[num] == "1":
      cntNumOne += 1  

# 첫 원소에 대해 처리
if s[0] == "0":
  cntNumZero += 1
if s[0] == "1":
  cntNumOne += 1

if cntNumZero < cntNumOne:
  print(cntNumZero)
else:
  print(cntNumOne)
