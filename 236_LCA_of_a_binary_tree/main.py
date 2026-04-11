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

def find(root, val):
    if not root: return None
    if root.val == val: return root
    return find(root.left, val) or find(root.right, val)

# Tree: [3,5,1,6,2,0,8,None,None,7,4]
root = build([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])

tests = [
    (5, 1, 3),
    (5, 4, 5),
]

for pv, qv, expected in tests:
    p, q = find(root, pv), find(root, qv)
    got = s.lowestCommonAncestor(root, p, q)
    status = "PASS" if got.val == expected else "FAIL"
    print(f"{status} | LCA({pv},{qv}): got={got.val} | expected={expected}")
