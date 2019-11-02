# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        
        result = []
        q = [root]
        i = 0
        while True:
            elem = q[i]
            i += 1
            if elem == 'null':
                result.append(elem)
                if i == len(q):
                    break
                continue
            else:
                result.append(str(elem.val))
            
            if elem.left is None:
                q.append('null')
            else:
                q.append(elem.left)
            
            if elem.right is None:
                q.append('null')
            else:
                q.append(elem.right)
                
            if i == len(q):
                break
                
        result = ','.join(result)
        return result
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        data = data.split(',')
        
        head = TreeNode(int(data[0]))
        current_level = [head]
        
        i = 1
        while i < len(data):
            next_level = []
            for node in current_level:
                if data[i] != 'null':
                    node.left = TreeNode(int(data[i]))
                    next_level.append(node.left)
                    
                if data[i + 1] != 'null':
                    node.right = TreeNode(int(data[i + 1]))
                    next_level.append(node.right)
                i += 2
                
            current_level = next_level
        
        return head
    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))