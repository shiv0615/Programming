'''
https://leetcode.com/problems/n-ary-tree-preorder-traversal/solution/
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)



Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]


Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000.


Follow up: Recursive solution is trivial, could you do it iteratively?
'''

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return None
        values = [root.val]
        def preorder_helper(root, values):
            if not root.children: return values
            for child in root.children:
                values.append(child.val)
                preorder_helper(child, values)
            return values
        return preorder_helper(root, values)