class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # res = defaultdict(int)
        # for num in nums:
        #     res[num] = 1 + res.get(num, 0)
        #     if num in res:
        #         res[num] += 1
        # res = sorted(res,key=res.get, reverse = True)[:k]
        # return res

        # Total Time Complexity: O(nlogn)
        # Total Space Complexity: O(n)

        #------------------------------------
        # Fastest [Bucket sort]
        # Total Time Complexity: O(n)
        # Total Space Complexity: O(n)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
