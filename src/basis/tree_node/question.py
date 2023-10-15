
import unittest
from typing import List, Optional

"""
算法：二叉树、N叉树、先序遍历、中序遍历、后序遍历、迭代实现、前序遍历
功能：
参考：
题目：

===================================力扣===================================
94. 二叉树的中序遍历（https://leetcode.cn/problems/binary-tree-inorder-traversal/description/）中序遍历迭代写法
144. 二叉树的前序遍历（https://leetcode.cn/problems/binary-tree-preorder-traversal/description/）前序遍历迭代写法
145. 二叉树的后序遍历（https://leetcode.cn/problems/binary-tree-postorder-traversal/）后序遍历迭代写法

===================================AcWing===================================
19. 二叉树的下一个节点（https://www.acwing.com/problem/content/description/31/）使用中序遍历找到其节点后序下一个


"""


class Solution:
    def __int__(self):
        return

    @staticmethod
    def lc_145(root: Optional[TreeNode]) -> List[int]:
        return TreeOrder().post_order(root)

    @staticmethod
    def lc_94(root: Optional[TreeNode]) -> List[int]:
        return TreeOrder().in_order(root)

    @staticmethoda
    def lc_144(root: Optional[TreeNode]) -> List[int]:
        return TreeOrder().pre_order(root)

