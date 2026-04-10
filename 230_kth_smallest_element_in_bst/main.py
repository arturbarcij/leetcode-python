from solution import Solution, TreeNode

s = Solution()

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
    ([3, 1, 4, None, 2], 1, 1),
    ([3, 1, 4, None, 2], 2, 2),
    ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
]

for vals, k, expected in tests:
    got = s.kthSmallest(build(vals), k)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | k={k} | got={got} | expected={expected}")
