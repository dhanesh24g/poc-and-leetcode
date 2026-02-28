from typing import List
from collections import defaultdict


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