from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            anagram_dict[key].append(s)
        return(list(anagram_dict.values()))
    
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)- ord('a')] +=1
            anagram_dict[tuple(count)].append(s)
        return(list(anagram_dict.values()))

if __name__ == "__main__":
    sol = Solution()
    result = sol.groupAnagrams1(["act","pots","tops","cat","stop","hat"])
    print(result)