'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 
'''
class Solution(object):
    def strStr(self, haystack, needle):
        needleLength  = len(needle)
        stacklength = len(haystack) - needleLength + 1
        i = 0
        k = needleLength
        j = 0
        answer = False
        while i < stacklength:
            newStr = haystack[j:k]
            if newStr == needle:
                return j
                answer = True
            k = k + 1
            i = i + 1
            j = j + 1
        if answer == False:
            return -1







answer = Solution()
result = answer.strStr("hello","ll")
print(result)