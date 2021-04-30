def solution(people, limit):
    people.sort()
    cnt=0
    a=0
    b=len(people)-1
    while a<=b:
        if a==b:
            cnt+=1
            break
        if limit>=people[a]+people[b]:
            a+=1
        b-=1
        cnt+=1
            
    return cnt
