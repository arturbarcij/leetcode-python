from solution import Solution, TreeNode

s = Solution()

# Helper to build a tree from a list (level-order, None = missing node)
def build(vals):
    if not vals:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in vals]
    for i, node in enumerate(nodes):
        if node:
            left_i, right_i = 2*i+1, 2*i+2
            if left_i < len(nodes): node.left = nodes[left_i]
            if right_i < len(nodes): node.right = nodes[right_i]
    return nodes[0]

tests = [
    ([2, 1, 3],             True),   # valid BST
    ([5, 1, 4, None, None, 3, 6],  False),  # 4 in right subtree but < 5
    ([1],                   True),   # single node
    ([5, 4, 6, None, None, 3, 7],  False),  # 3 in right subtree of 5 but < 5
]

for vals, expected in tests:
    got = s.isValidBST(build(vals))
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | tree={vals} | got={got} | expected={expected}")
