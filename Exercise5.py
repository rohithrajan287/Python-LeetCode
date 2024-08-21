'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        length = len(strs)
        i = 0
        a = []
        y = 0
        newStr = ""
        while i < length:                               #["flower","f","flight"]
            x = [i for i in strs[i]]
            len1 = len(x)
            if y < len1:
                a.append(x[y])
                i = i + 1
                if(i == 3):
                    notSame = "not failed"
                    y = y + 1
                    i = 0
                    for each in a:
                        if each != a[0]:
                            notSame = "failed"
                    if notSame == "not failed":
                        newStr = newStr + a[0]
                    if notSame == "failed":
                        return newStr
                    a = []
            else:
                return newStr



answer = Solution()
result = answer.longestCommonPrefix(["flower","f","flight"])
#result = answer.longestCommonPrefix(["dog","racecar","car"])
print(result)
