# from typing import List
# def runningSum( nums: List[int]) -> List[int]:
#     for i in range(1,len(nums)):
#         nums[i] += nums[i-1]
#     return nums
# nums = [1,2,3,4,5]
# print(runningSum(nums))

# nums = [1,2,3,4,5]
# res = [0] *(len(nums))
# for i in range(len(nums)):
#     curr_sum = 0 
#     for j in range(0,i+1):
#         curr_sum += nums[j]
#     res[i] = curr_sum
# print(res)


# def largestAltitude(self, gain: List[int]) -> int:
    # n = len(gain)
    # res = [0] * (n+1)
    # for i in range(1,n+1):
    #     res[i] = res[i-1]+gain[i-1]
    # return max(res)


    # c_alt,m_alt = 0,0
    # for i in gain:
    #     c_alt += i
    #     m_alt = max(c_alt,m_alt)
    # return m_alt

from typing import List
def findMiddleIndex(nums: List[int]) -> int:
    total = sum(nums)
    left_sum = 0
    for i in range(0,len(nums)):
        right = total - nums[i] - left_sum
        if left_sum == right:
            return i
        left_sum += nums[i]
    return -1
nums = [2,3,-1,8,4]
print(findMiddleIndex(nums))