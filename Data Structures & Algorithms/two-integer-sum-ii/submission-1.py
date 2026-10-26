class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(numbers,1):
            if target - n in seen:
                return [seen[target - n], i]
            # key = number, value = index    
            seen[n] = i
