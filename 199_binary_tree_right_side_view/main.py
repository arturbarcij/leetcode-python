from solution import Solution, TreeNode

s = Solution()

# Tree 1:    1
#           / \
#          2   3
#           \
#            5
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(5)

# Tree 2:   1
#            \
#             3
root2 = TreeNode(1)
root2.right = TreeNode(3)

# Tree 3: empty
root3 = None

# Tree 4: single node
root4 = TreeNode(1)

tests = [
    (root1, [1, 3, 5]),
    (root2, [1, 3]),
    (root3, []),
    (root4, [1]),
]

for root, expected in tests:
    got = s.rightSideView(root)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | got={got} | expected={expected}")
