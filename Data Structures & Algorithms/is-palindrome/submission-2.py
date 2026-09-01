import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove all whitespace and non-alphanumeric characters
        restr = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # or loop and check with .isalnum() = a-zA-Z0-9
        return restr == restr[::-1]