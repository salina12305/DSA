class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class Solution:
    def maxPowerGeneration(self, root):
        self.maximum = -10**9  
        def findMax(node):
            if node is None:
                return 0
            left = findMax(node.left)
            right = findMax(node.right)
            if left < 0:
                left = 0
            if right < 0:
                right = 0
            total = node.value + left + right

            if total > self.maximum:
                self.maximum = total
            return node.value + max(left, right)

        findMax(root)
        return self.maximum
    
if __name__ == "__main__":
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solver = Solution()
    answer = solver.maxPowerGeneration(root)

    print("-" * 40)
    print("Maximum Net Power Generation:", answer)
    print("Explanation: 15 + 20 + 7 = 42 (negative value -10 is ignored)")
    print("-" * 40)