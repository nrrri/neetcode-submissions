import re
import math
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove all whitespace and non-alphanumeric characters
        restr = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        halflen = math.ceil(len(restr) / 2)
        first = restr[halflen:]
        if (len(restr) % 2 == 1):
            last = restr[:halflen - 1]
        else:
            last = restr[:halflen]
        last = last[::-1]
        print(first)
        print(last)
        return first == last