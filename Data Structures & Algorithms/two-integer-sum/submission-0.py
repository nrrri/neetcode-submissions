class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # l+r = target
        # l = target - r
        # if l in prevMap return
        # if not store l in prevMap (val,index)

        prevMap = {}
        for i , r in enumerate(nums):
            diff = target - r
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[r] = i