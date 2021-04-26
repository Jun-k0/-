def solution(progresses, speeds):
    answer = []
    time=0        #time 방식
    count=0
    while len(progresses)>0:
        if progresses[0]+(time*speeds[0])>=100:
            progresses.pop(0)
            speeds.pop(0)
            count+=1
        else:
            if count>0:
                answer.append(count)
                count=0
            else:
                time+=1
    answer.append(count)
    return answer
  
  '''
  pop(0) - 첫번째 원소 pop : 데이터 지운 후 당겨오기 때문에 O(n)
  deque.popleft() : O(1) 걸리므로 더 빠르당
  '''
