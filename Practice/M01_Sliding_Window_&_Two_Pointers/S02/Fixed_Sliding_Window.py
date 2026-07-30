from typing import List

def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    win_sum = sum(arr[0:k])
    count = 0
    if (win_sum/k) >= threshold:
        count += 1
    n = len(arr)
    for i in range(n-k):
        win_sum = win_sum - arr[i] + arr[k+i]
        if (win_sum/k) >= threshold:
            count += 1
    return count
arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
print(numOfSubarrays(arr,k,threshold))