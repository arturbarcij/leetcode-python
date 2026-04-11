from solution import Solution, TreeNode

s = Solution()

def to_list(root):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val if node else None)
        if node:
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result

tests = [
    ([3,9,20,15,7], [9,3,15,20,7], [3,9,20,None,None,15,7]),
    ([1,2],         [2,1],         [1,2]),
    ([-1],          [-1],          [-1]),
]

for preorder, inorder, expected in tests:
    got = to_list(s.buildTree(preorder, inorder))
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | got={got} | expected={expected}")
