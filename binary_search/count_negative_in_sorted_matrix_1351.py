from typing import List

# store the n of each array
# do binary search to get first negative value (key)
# first negative value can we get it if its previouse element is > 0 and the value < 0
# so we create function to tell if it first negative value or not
# else continue our binary search
# if fount it we increase count with n - index


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        n = len(grid[0])
        count = 0

        def is_first_negative(nums, index):
            if nums[index] < 0 and (index == 0 or nums[index - 1] >= 0):
                return True
            return False

        def binary_search(arr):

            l, r = 0, n - 1

            while l <= r:
                mid = (l + r) // 2
                if is_first_negative(arr, mid):
                    return mid
                elif arr[mid] >= 0:
                    l = mid + 1
                else:
                    r = mid - 1
            return n

        for arr in grid:
            count += n - binary_search(arr)
        return count


x = Solution()
y = x.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]])
print()
