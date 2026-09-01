class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # check if K in len(nums)
        # slice into 2 array
        # before k -> move to the back
        # after k -> shift to the front
        
        nums[:] = nums[-k % len(nums):] + nums[:-k % len(nums)]
        # THIS WAY THE BEST, TIME COMPLEX = O(n)