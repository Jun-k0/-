def solution(n):
    answer = ""
    arr=[1,2,4]
    cnt=1
    val=4
    while True:
        if n<val:
            val-=3**cnt
            temp=n-val
            while cnt>0:
                cnt-=1
                if temp//(3**cnt)>=1: 
                    answer+=str(arr[temp//(3**cnt)]) # str 합치기
                    temp%=3**cnt
                else:
                    answer+="1"
            break
        else:
            cnt+=1
            val+=3**cnt
    return answer
  '''
  1 2 3의 삼진법 풀이도 
  '''
