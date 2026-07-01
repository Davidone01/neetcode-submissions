# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        first =  second =  prev= None
        def inorder(node):
            nonlocal first,second, prev
            if node is None:
                return #non possiamo più andare avanti
            inorder(node.left) #andiamo a sinistra
            #ora siamo nel nodo verifichiamo se c'è conflitto
            if prev is not None and prev.val>node.val:
                if first is None:
                    first = prev # solo prima volta
                second = node #always
            prev = node # così nei cicli successivi si può controllare

            inorder(node.right)

        inorder(root)
        tmp = first.val
        first.val = second.val
        second.val = tmp
