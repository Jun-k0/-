def solution(n,a,b):
    answer = 0
    cnt=1
    while True:
        n=n//2
        if (n>=a and n<b) or (n>=b and n<a):
            while n>1:
                n=n//2
                cnt+=1
            answer=cnt
            break
        elif n<a and n<b:
            a-=n
            b-=n
            
    return answer
