from solution import Solution

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

# BST: [6,2,8,0,4,7,9]
root = build([6, 2, 8, 0, 4, 7, 9])

tests = [
    (2, 8, 6),
    (2, 4, 2),
    (0, 5, None),  # 5 doesn't exist, skip
]

for pv, qv, expected in tests:
    p, q = find(root, pv), find(root, qv)
    if p is None or q is None:
        print(f"SKIP | p={pv} or q={qv} not in tree")
        continue
    got = s.lowestCommonAncestor(root, p, q)
    status = "PASS" if got.val == expected else "FAIL"
    print(f"{status} | LCA({pv},{qv}): got={got.val} | expected={expected}")
