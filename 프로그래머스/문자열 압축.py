def solution(s):
    answer = 1000
    
    # 길이가 1일때 예외 추가
    if len(s) == 1:
        answer = 1
    
    for unit in range(1, len(s)):
        arr = []
        for i in range(0, len(s), unit):
            if len(arr) != 0:
                if s[i:i+unit] == arr[-1]:
                    arr[-2] += 1
                    continue
                    
            arr.append(1)
            arr.append(s[i:i+unit])
        
        temp = 0
        for i in range(len(arr)):
            if i%2 == 0:
                if arr[i] != 1:
                    temp += len(str(arr[i]))
            if i%2 == 1:
                temp += len(arr[i])
                
        #print(arr, temp)
        
        answer = min(answer, temp)
            
    return answer
