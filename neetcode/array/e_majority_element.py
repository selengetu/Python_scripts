from collections import defaultdict
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = defaultdict(int)
        maxVal = res = 0
        for n in nums:
            count[n] +=1
            if maxVal < count[n]:
                maxVal = count[n]
                res = n
        return res
