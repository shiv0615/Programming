

'''
https://leetcode.com/problems/container-with-most-water/
Nicely explained solution - take a look at the Leet Code video
Medium

14063

850

Add to List

Share
You are given an integer array height of length n. There are n vertical lines drawn such that the
two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
'''

class Solution:
    def maxArea(self, height):
        area=0
        i=0
        j=len(height)-1

        while i<j:
            minh=min(height[i],height[j])
            ar=minh*(j-i)
            area=max(area,ar)

            if height[i]>height[j]:
                j-=1
            else:
                i+=1

        return(area)

tests = [[1,8,6,2,5,4,8,3,7], [1,2,1], [1,1]]
for test in tests:
    sol = Solution()
    print(f'Container with Max Water for {test} is {sol.maxArea(test)}')