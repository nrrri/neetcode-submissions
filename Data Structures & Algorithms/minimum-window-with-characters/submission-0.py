class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        result, resLen = [-1, -1], float("infinity")
        countT, window = {}, {}
        # set countT to 1
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        l = 0
        # increase r until last
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update result
                if (r - l + 1) < resLen:
                    result = [l, r]
                    resLen = r - l + 1
                # pop from the left of window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = result
        return s[l : r + 1] if resLen != float("infinity") else ""
