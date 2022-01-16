from collections import deque

n = int(input())
arr = list(map(int, input().split()))
group = 0

arr.sort()
warriors = deque(arr)

while warriors:
  nowFear = warriors.popleft()
  cnt = nowFear - 1
  
  # 현재 모험가의 공포도만큼 팀원 추가
  while cnt and warriors:
    nextFear = warriors.popleft()
    if nextFear > nowFear:
      cnt += nextFear - nowFear
      nowFear = nextFear
    cnt -= 1

  # 그룹이 결성 됐으면 그룹 수 +1
  if cnt == 0:
    group += 1

print(group)
