from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}
        for i , num in enumerate(nums):
            if target - num not in map:
                map[num] = i
            else :
                return [i,map[target - num]]
            
obj = Solution()
obj.twoSum([2,7,11,15],9)