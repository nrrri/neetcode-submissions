class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort then compare arr
        return sorted(s) == sorted(t)