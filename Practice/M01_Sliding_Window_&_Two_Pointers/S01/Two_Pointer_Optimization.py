'''
input: [12,45,63,20,96,25,10]
output: [12,20,96,10]



nums = list(map(int,input().split()))
res = []
for ele in nums:
    if ele%2==0:
        res.append(ele)
print(res)
'''
# arr=list(map(int,input().split()))
# i=0
# for j in range(len(arr)):

