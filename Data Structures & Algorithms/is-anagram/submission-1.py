class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # sort then compare arr
        # return sorted(s) == sorted(t) # not efficient

        # solution 2
        countS, countT = {},{}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0) # 0 is default val if couldn't get value
            countT[t[i]] = 1 + countT.get(t[i],0)
        print(countS, countT)
        for c in countS:
            # print(countS[c],countT.get(c,0))
            if countS[c] != countT.get(c,0):
                return False
        return True