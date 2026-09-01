class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        setNums = {}
        for idx, num in enumerate(nums):
            setNums[num] = idx

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in setNums and setNums[diff] != idx:
                return [idx, setNums[diff]]
        return []
        