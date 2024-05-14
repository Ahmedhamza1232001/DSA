from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix , suffix , result = n * [1] , n *[1] ,n * [1]
        
        
        #1 2 3 4
        #1 2 12 24
        for i in range(n):
            #fill the prefix 
            prefix[i] = nums[i] * (prefix[i-1] if i  > 0 else 1)

        #1 2 3 4
        #24  24  12  4
        for i in range(n - 1,-1,-1):
            #fill the suffix 
            suffix[i] = nums[i] * (suffix[i+1] if i+1 < n else 1)

        print(prefix)
        print(suffix)

    #arr        1   2   3   4
    #prefix     1   2   6  24
    #suffix     24 24  12   4

        #fill the result list
        for i in range(n):

            if i > 0:
                result[i] *= prefix [i-1]
            
            if i < n-1:
                result[i] *= suffix [i+1]
        
        return result

    
x = Solution()
x.productExceptSelf([1,2,3,4])