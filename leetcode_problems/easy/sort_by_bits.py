from typing import List
from collections import defaultdict

"""Problem Statement:
You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.
"""

def sortByBits(arr: List[int]) -> List[int]:

    print("Input:", arr)
    dicts = defaultdict(list)
    for num in arr:
        cnt = num.bit_count()
        dicts[cnt].append(num)
    tmp = sorted(list(dicts))
    ans = []
    for num in tmp:
        ans += sorted(dicts[num])

    return ans


print("Output:", sortByBits(arr=[0,1,2,11,9,15,3,4,5,6,7,8]))