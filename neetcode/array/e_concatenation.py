from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [0] * 2 * l

        for i, n in enumerate(nums):
            ans[i] = n
            ans[i+l] = n
        return ans


    nums = [1, 2, 3]
    sol = Solution()
    result = sol.getConcatenation(nums)
    print(result)