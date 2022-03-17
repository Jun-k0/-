## Trie 풀이

class Node:
  def __init__(self, data):
    self.data = data
    self.child = {}
    self.last = False	# 마지막 원소인지 확인

class Trie:
  def __init__(self):
    self.root = Node('')

  def insert(self, nums):
    nowNode = self.root
    
    for num in nums:
      if num in nowNode.child:
        nowNode = nowNode.child[num]
      else:
        newNode = Node(num)
        nowNode.child[num] = newNode
        nowNode = newNode
        
    nowNode.last = True

  # 접두어인지 확인하는 메소드
  def isPrefix(self, phone):
    nowNode = self.root
    
    for num in phone:
      if nowNode.last == True:
        return False
        
      if num in nowNode.child:
        nowNode = nowNode.child[num]

    return True
        
t = int(input())

for _ in range(t):
  phones = []
  n = int(input())
  trie = Trie()
  result = 1
  
  for i in range(n):
    tmp = input()
    phones.append(tmp)
    trie.insert(tmp)

  for phone in phones:
    result *= trie.isPrefix(phone)

  if result:
    print("YES")
  else:
    print("NO")
    
## 정렬 풀이
t = int(input())

def sol(phones):
  
  for i in range(len(phones)-1):
    phoneLength = len(phones[i])
    if phones[i] == phones[i+1][:phoneLength]:
        print("NO")
        return

  print("YES")

for _ in range(t):
  phones = []
  n = int(input())
  
  for i in range(n):
    phones.append(input())

  phones.sort()
  sol(phones)
