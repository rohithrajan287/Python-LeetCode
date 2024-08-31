'''
Given a string s, find the length of the longest 
substring
 without repeating characters.
 
'''

class Solution(object):
    def lengthOfLongestSubstring(self,s):
        arr = [i for i in s]
        newStr = []
        longStr = []
        for a in arr:
            if a not in newStr:
                newStr = newStr + [a]
            else:
                if len(newStr) > 1:
                    if len(newStr) > len(longStr):
                        longStr = newStr
                newStr = [a]
        if len(longStr) > len(newStr):
            s = s = ''.join(longStr)
            return len(s)
        else:
            s = s = ''.join(newStr)
            return len(s)




answer = Solution()
result = answer.lengthOfLongestSubstring("abcgabuua")
print(result)