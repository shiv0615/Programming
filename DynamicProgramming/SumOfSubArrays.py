class Solution:
    def maxSubArray_brute_force(self, nums):
        max_sum = -999999999
        if len(nums) == 1: return nums[0]
        for i in range(len(nums)):
            sumnum = 0
            for j in range(len(nums)-i):
                sumnum += nums[j]
                max_sum = max(sumnum, max_sum)
            sumnum = 0
            for j in range(i, len(nums)):
                sumnum += nums[j]
                max_sum = max(sumnum, max_sum)
            sumnum = 0
            for j in range(i, len(nums)-1):
                sumnum += nums[j]
                max_sum = max(sumnum, max_sum)
        return max_sum

    def maxSubArray(self, nums):
        max_sum = -99999
        sum     = 0
        n = len(nums)
        if n == 0: return 0
        elif n == 1: return nums[0]
        elif n == 2: return (nums[0] + nums[1])
        else:
            sum += self.maxSubArray(nums[:int(n/2)])
            sum+= self.maxSubArray(nums[int(n/2):])
            max_sum = max(max_sum, sum)
            print(f'sum:{sum}, max_sum: {max_sum}, n:{n}, int(n/2):{int(n / 2)}, '
                  f'nums[:int(n/2)]:{nums[:int(n / 2)]},nums[int(n/2):]:{nums[int(n / 2):]}')
        return max_sum

    def Online_maxSubArray(self, nums):
        current, result = nums[0], nums[0]
        for i in range(1, len(nums)):
            current = max(current + nums[i], nums[i] )
            result = max(current, result)
        return result

def main():
    num = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # num = [1]
    # num = [5, 4, -1, 7, 8]
    brut_sum = Solution().maxSubArray_brute_force(num)
    div_sum  = Solution().Online_maxSubArray(num)
    print('Sum: ', brut_sum, div_sum)

if __name__ =='__main__':
    main()