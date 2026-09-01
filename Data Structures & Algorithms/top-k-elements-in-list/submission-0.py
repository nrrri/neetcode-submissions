class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for num in nums:
            res[num] += 0
            if num in res:
                res[num] += 1
        print('sorted',sorted(res,key=res.get, reverse = True))
        res = sorted(res,key=res.get, reverse = True)[:k]
        print(res)
        return res