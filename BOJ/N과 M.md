# 백트래킹?
해를 찾는 도중 아니라면, 되돌아가서 다시 해를 찾아가는 기법

# N과 M
대표적 백트래킹 문제들이다. 조금 더 간결한 코드를 작성할 수 있지만, 좀 더 복잡한 문제에서도 풀기 위해 visit 리스트를 추가해 풀었다.

## N과 M (1)
https://www.acmicpc.net/problem/15649
- 조건 : 중복되면 안된다.
```python
n, m = map(int, input().split())

visit = [False for _ in range(n+1)]

def sol(level, ansList):
  if level > m:
    print(' '.join(map(str, ansList)))
    return

  for i in range(1, n+1):
    if not visit[i]:
      visit[i] = True
      ansList.append(i)
      sol(level+1, ansList)
      ansList.pop()
      visit[i] = False

sol(1, [])
```
```python
# 4 2
1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3
```

## N과 M (2)
https://www.acmicpc.net/problem/15650
- 조건 : 중복되면 안되며, 오름차순이어야함.
```python
n, m = map(int, input().split())

visit = [False for _ in range(n+1)]

def sol(level, ansList):
  if level > m:
    print(' '.join(map(str, ansList)))
    return

  for i in range(1, n+1):
    if not visit[i]:
      if ansList:
        if ansList[-1] >= i:
          continue
      visit[i] = True
      ansList.append(i)
      sol(level+1, ansList)
      ansList.pop()
      visit[i] = False

sol(1, [])
```
```python
# 4 2
1 2
1 3
1 4
2 3
2 4
3 4
```

## N과 M (3)
https://www.acmicpc.net/problem/15651
- 조건 : 중복 가능
```python
n, m = map(int, input().split())

visit = [False for _ in range(n+1)]

def sol(level, ansList):
  if level > m:
    print(' '.join(map(str, ansList)))
    return

  for i in range(1, n+1):
    ansList.append(i)
    sol(level+1, ansList)
    ansList.pop()

sol(1, [])
```
```python
# 4 2
1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
4 4
```

## N과 M (4)
https://www.acmicpc.net/problem/15652
- 조건 : 중복 가능하며, 같거나 오름차순
```python
n, m = map(int, input().split())

visit = [False for _ in range(n+1)]

def sol(level, ansList):
  if level > m:
    print(' '.join(map(str, ansList)))
    return

  for i in range(1, n+1):
    if ansList:
      if ansList[-1] > i:
        continue
    ansList.append(i)
    sol(level+1, ansList)
    ansList.pop()

sol(1, [])
```
```python
# 3 3
1 1 1
1 1 2
1 1 3
1 2 2
1 2 3
1 3 3
2 2 2
2 2 3
2 3 3
3 3 3
```
