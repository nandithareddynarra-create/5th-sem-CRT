# from typing import List

# def totalFruit( fruits: List[int]) -> int:
#     left,ans = 0,0
#     freq = {}

#     for right in range(len(fruits)):
#         freq[fruits[right]] = freq.get(fruits[right],0)+1

#         while len(freq) > 2:
#             freq[fruits[left]] -= 1
#             if freq[fruits[left]] == 0:
#                 del freq[fruits[left]]
#             left += 1

#         ans = max(ans, right - left + 1)

#     return ans
# fruits = 



def lengthOfLongestSubstring(s: str) -> int:
    left,max_len = 0,0
    se = set()
    for right in range(len(s)):
        while s[right] in se:
            se.remove(s[left])
            left += 1
        se.add(s[right])
        max_len = max(max_len, right-left+1)
    return max_len
s = "aaabc"
print(lengthOfLongestSubstring(s))
