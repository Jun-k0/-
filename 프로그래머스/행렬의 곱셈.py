def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        ans=[]
        for j in range(len(arr2[0])):
            cnt=0
            for k in range(len(arr1[0])):
                cnt+=arr1[i][k]*arr2[k][j]
            ans.append(cnt)
        answer.append(ans)
    return answer
