class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        need = {}
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1

        window = {}
        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1  # char entering
            if r >= m:  # window too big: drop left char
                out = s2[r - m]
                window[out] -= 1
                if window[out] == 0:
                    del window[out]  # keep dict comparison correct
            if window == need:
                return True
        return False
