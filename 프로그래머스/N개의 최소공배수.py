def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

def solution(arr):
    answer = 0
    arr.sort()
    val=arr[0]
    for i in arr:
        val=(i*val)//gcd(i,val)
    answer=val
    return answer
