from typing import List

"""Problem Statement:
You are given an integer array nums of length n.

An array is trionic if there exist indices 0 < p < q < n − 1 such that:

nums[0...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...n − 1] is strictly increasing.
Return true if nums is trionic, otherwise return false.
"""

def isTrionic(nums: List[int]) -> bool:

    print("Input:", nums)

    if len(nums) <= 3:
        return False

    stop = 0
    p = q = r = False
    for i in range(len(nums) - 1):
        if nums[i + 1] > nums[i]:
            p = True
        elif nums[i + 1] < nums[i]:
            stop = i
            break
        else:
            return False

    for i in range(stop, len(nums) - 1):
        if nums[i + 1] < nums[i]:
            q = True
        elif nums[i + 1] > nums[i]:
            stop = i
            break
        else:
            return False

    for i in range(stop, len(nums) - 1):
        if nums[i + 1] > nums[i]:
            r = True
        else:
            return False

    return p and q and r


print("Result:", isTrionic([1,3,5,4,2,6]))