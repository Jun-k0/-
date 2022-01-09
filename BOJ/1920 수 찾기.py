def binarySearch(arr, start, end, target):
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == target:
      return 1
    elif arr[mid] < target:
      start = mid + 1
    elif arr[mid] > target:
      end = mid - 1

  return 0

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

for target in arr2:
  chk = binarySearch(arr1, 0, n-1, target)
  print(chk)
