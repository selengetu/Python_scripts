from collections import defaultdict
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)

        basket = [[] for i in range(len(nums) + 1)]
        for n in nums:
            freq[n] +=1
        
        for num,count in freq.items():
            basket[count].append(num)
        
        res = []
        
        for i in range(len(basket)-1, 0, -1):
            for number in basket[i]:
                res.append(number)
                if len(res) == k:
                    return res
