class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k = 1...max num in plie
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = l + ((r - l) // 2)
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:  # ** want
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res
