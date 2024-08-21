'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''


class Solution(object):
    def isValid(self, s):
       x = [i for i in s]
       a = []                                      
       b = []
       if(len(x) <= 1) or x[0] == "]" or x[0] == ")" or x[0] == "}" :
           return False
       for i in x:
           if i == "(" or i == "{" or i == "[":
               a.append(i)
           if i == ")":
               if "(" in a:
                   length = len(a)
                   if int(length) > 1:
                       if a[length-1] == "(":
                           a.pop()
                       else:
                        return False
                   else:
                       a.pop()
               else:
                    return False
           if i == "}":
               if "{" in a:
                   length = len(a)
                   if length > 1:
                       if a[length - 1] == "{":
                           a.pop()
                       else:
                           return False
                   else:
                      a.pop()
               else:
                    return False
           if i == "]":
               if "[" in a:
                   length = len(a)
                   if length > 1:
                       if a[length - 1] == "[":
                           a.pop()
                       else:
                           return False
                   else:
                       a.pop()
               else:
                    return False
       if a != []:
           return False
       else:
           return True



answer = Solution()
result = answer.isValid("({)}[")
print(result)
