'''
Remove Duplicates
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
''' 

class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        x = len(nums)
        for j in range(1, x):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
        
        
answer = Solution()
result = answer.removeDuplicates(['1','1','2'])
print(result)