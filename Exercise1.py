'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''


class Solution(object):
    def twoSum(self, nums, target):
        x = len(nums)
        for i in range(0,int(x)):
            for j in range(0,int(x)):
                if i != j:
                    if int(nums[i]) + int(nums [j]) == int(target):
                        return [i,j]






length = input("Enter the length of the array")
i = 0
nums = []
print(length)
while (i<int(length)):
    num = input(f"Enter the {i} value")
    i = i + 1
    nums.append(num)

target = input("What is the Target")
answer = Solution()
result = answer.twoSum(nums,target)
print(f"Position of two digits are {result}")
