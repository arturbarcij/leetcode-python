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
    ([3, 9, 20, None, None, 15, 7], True),
    ([1, 2, 2, 3, 3, None, None, 4, 4], False),
    ([], True),
]

for vals, expected in tests:
    got = s.isBalanced(build(vals))
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | got={got} | expected={expected}")
