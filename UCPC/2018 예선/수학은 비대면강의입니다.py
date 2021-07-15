import sys

input=sys.stdin.readline

arr = list(map(int,input().split()))
# 012 345

y=(arr[2]*arr[3]-arr[0]*arr[5])//(arr[1]*arr[3]-arr[0]*arr[4])
x=(arr[2]*arr[4]-arr[1]*arr[5])//(arr[0]*arr[4]-arr[1]*arr[3])

print(int(x),int(y))

'''
arr로 받지말고 a,b,c,d,e,f로 받았으면 더 편했을듯함
연산같은거 할때 웬만하면 나누지말고 곱하자
'''
