class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(ch for ch in s if ch.isalnum()).lower()

        return clean[::-1] == clean
