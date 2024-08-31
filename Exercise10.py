'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.


'''

class Solution(object):
    def searchInsert(self, nums, target):
        i = 0
        for digit in nums:
            if digit == target:
                return i
            if digit > target:
                return i
            i = i + 1
        return len(nums)


answer = Solution()
result = answer.searchInsert([1,3,5,6],4)
print(result)