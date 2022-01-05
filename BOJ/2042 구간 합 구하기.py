def make_tree(start, end, node):
  if start == end:
    tree[node] = data[start]
    return tree[node]
    
  mid = (start + end) // 2
  tree[node] = make_tree(start, mid, node * 2) + make_tree(mid+1, end, node * 2 + 1)
  return tree[node]

def sum(start, end, node, left, right):
  if start > end:
    return 0
  if start > right or end < left:
    return 0
  if start >= left and end <= right:
    return tree[node]
  mid = (start + end) // 2
  return sum(start, mid, node * 2, left, right) + sum(mid + 1, end, node * 2 + 1, left, right)

def update(start, end, node, idx, diff):
  if start > idx or end < idx:
    return;
  if start <= idx <= end:
    tree[node] += diff
  if start == end:
    return;
  
  mid = (start + end) // 2
  update(start, mid, node * 2, idx, diff)
  update(mid + 1, end, node * 2 + 1, idx, diff)

n,m,k = map(int,input().split())

data = []
tree = [-1] * (n * 4)

for _ in range(n):
  data.append(int(input()))

make_tree(0, n-1, 1)
#print(data)
#print(tree)

for _ in range(m+k):
  a, b, c = map(int,input().split())
  if a == 1:
    update(0, n-1, 1, b-1, c - data[b-1])
    data[b-1] = c
  if a == 2:
    print(sum(0, n-1, 1, b-1, c-1))
  #print(data)
  #print(tree)
