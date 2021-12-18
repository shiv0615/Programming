import numpy as np

class Solution:
    def __init__(self, price):
        self.prices = price
        self.n      = len(price)

    def maxProfit(self):
        maxdiff = []
        for i in range(self.n):
            maxval = -9999
            for j in range(i+1,self.n):
                maxval = max(-self.prices[i]+self.prices[j],maxval)
            maxdiff.append(maxval)
        return self.prices[maxdiff.index(max(maxdiff))]

    def maxProfit_narray(self):
        n = len(self.prices)
        prices = np.array(self.prices)
        diff = prices[1:] - prices[:n - 1]
        print(prices, diff)
        maxval  = -9999
        for i in range(1, n):
            maxval = max(maxval,np.sum(diff[i:]))
        if np.max(maxval) > 0:
            return np.max(maxval)
        else:
            return 0

class AddNumberStrings():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add_two_nums(self):
        num1 = self.num1
        num2 = self.num2
        lendiff = abs(len(num2) - len(num1))
        if len(num1) < len(num2):
            num1 = '0' * lendiff + num1
        elif len(num2) < len(num1):
            num2 = '0' * lendiff + num2
        sum = 0
        for i in range(len(num2) - 1, -1, -1):
            power = len(num2) - 1 - i
            x1 = ord(num1[i]) - ord('0')
            x2 = ord(num2[i]) - ord('0')
            print('i, x1, x2, power ', i, x1, x2, power)
            sum = sum + (x1 + x2) * (10 ** power)
        return str(sum)

if __name__ =='__main__':
    price = [7,1,5,3,6,4]
    sol = Solution(price)
    print(sol.maxProfit_narray())

    num1 = '123'
    num2 = '1111'
    addnumstr = AddNumberStrings(num1,num2)
    addnumstr.add_two_nums()
