# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root == None:
            return []
        
        traversal = [[root.val]]
        q = [root]
        
        while True:
            new_q = []
            level = []
            for p in q:
                if p.left != None:
                    level.append(p.left.val)
                    new_q.append(p.left)
                
                if p.right != None:
                    level.append(p.right.val)
                    new_q.append(p.right)
                
            if len(new_q) == 0:
                break
            
            q = new_q
            traversal.append(level)
          
        result = []
        for line in traversal:
            result.append(line[len(line) - 1])
        
        return result

    