class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap -> num : count
        # sort hashmap find the highest
        d = {}
        for num in nums:
            d[num] = d.get(num,0) +1 
        result = sorted(d, key=d.get, reverse=True)[:k]

        return result