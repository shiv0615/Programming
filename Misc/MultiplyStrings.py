'''
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or
convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        maxlen = max(n1, n2)
        num1 = num1.rjust(maxlen, '0')
        num2 = num2.rjust(maxlen, '0')
        a1 = 0
        a2 = 0
        for i in range(maxlen):
            a1 += (ord(num1[i]) - ord('0')) * (10 ** (maxlen - 1 - i))
            a2 += (ord(num2[i]) - ord('0')) * (10 ** (maxlen - 1 - i))
        result = a1 * a2
        str_result = []
        while 1:
            str_result.append(chr(ord('0') + result % 10))
            result = result // 10
            if result == 0: break
        concat_str_result = ''
        for i in range(len(str_result) - 1, -1, -1): concat_str_result += str_result[i]
        return concat_str_result

def main():
    num1='9'
    num2='99'
    sol = Solution()
    result = sol.multiply(num1=num1,num2=num2)
    print(result)

if __name__ =='__main__':
    main()