from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         
        if len(s) != len(t):
            return False
        

        strS, strT = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            strS[s[i]] +=1
            strT[t[i]] +=1
        return strS == strT

if __name__ == "__main__":
    s = "racecar"
    t = "carrace"

    sol = Solution()
    res = sol.isAnagram(s, t)

    print(res)