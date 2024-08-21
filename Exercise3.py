'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''




class Solution(object):
    def romanToInt(self, s):
        x = [i for i in s]
        res = 0
        length = len(x)
        i = 0
        while i < length:
            temp = x[i]     #IV  I - 1, V - 5    #MCMXCIV
            j = i + 1
            if j < length:
                nextTemp = x[j]
                if (temp == "I" and (nextTemp == "V" or nextTemp == "X")) or (temp == "X" and (nextTemp == "L" or nextTemp == "C")) or (temp == "C" and (nextTemp == "D" or nextTemp == "M")):
                    value1 = self.FindValue(temp)
                    value2 = self.FindValue(nextTemp)
                    value = int(value2) - int(value1)
                    i = i + 1
                else:
                    value = self.FindValue(temp)
            else:
                value = self.FindValue(temp)
            res = int(res) + int(value)
            i = i + 1
        return res

    def FindValue(self,c):
        values = {"I" : "1","V" : "5","X":"10","L":"50","C":"100","D":"500","M":"1000"}
        result = values[c]
        return result
		
		
		
callClass = Solution()
result = callClass.romanToInt("MCMXCIV")
print(f"result {result}")