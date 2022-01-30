class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # O(n.log(n))

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                continue

            target = -nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res