def getParent(n, parent):
    if n != parent[n]:
        parent[n] = getParent(parent[n], parent)
    return parent[n]

def union(a, b, parent):
    a = getParent(a, parent)
    b = getParent(b, parent)
    if a < b:
        parent[b] = a
    if a > b:
        parent[a] = b

def solution(n, costs):
    answer = 0
    parent = [0 for _ in range(n)]
    
    for i in range(n):
        parent[i] = i
    
    costs.sort(key=lambda x:x[2])
    
    for i in costs:
        s, e, cost = i[0], i[1], i[2]
        if getParent(s, parent) != getParent(e, parent):
            answer += cost
            union(s,e,parent)
    
    return answer
  
