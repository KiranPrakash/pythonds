"""
input:  arr = [8, 10, 2]
output: [20, 16, 80]
"""


def calcProductArray(nums):
    # p, q = 1, 1
    # results = [1] * len(nums)
    # for i in range(len(nums)):
    #     results[i] *= p
    #     results[~i] *= q
    #     p *= nums[i]
    #     q *= nums[~i]
    # return results

    p = 1
    n = len(nums)

    output = []

    for i in range(0,n):
        output.append(p)
        p *= nums[i]

    p=1
    for i in range(n-1,-1,-1):
        output[i] *= p
        p *= nums[i]


    return output



arr = [0]
x = calcProductArray(arr)
print(x)