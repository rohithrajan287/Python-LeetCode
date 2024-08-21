'''
Given an integer x, return true if x is a palindrome, and false otherwise.
'''




class Solution(object):
    def isPalindrome(self, x):
        inputNum = x
        newNum = 0
        while x > 0:
            newNum = newNum * 10 + x % 10
            x = int(x / 10)
        if newNum == inputNum:
            return True
        else:
            return False