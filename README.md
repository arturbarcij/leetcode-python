# LeetCode Python

A collection of LeetCode solutions in Python, focused on learning Data Structures and Algorithms.

## Progress

![Easy](https://img.shields.io/badge/Easy-14-brightgreen) ![Medium](https://img.shields.io/badge/Medium-25-yellow) ![Hard](https://img.shields.io/badge/Hard-7-red)

| Difficulty | Count |
|------------|-------|
| Easy       | 14    |
| Medium     | 25    |
| Hard       | 7     |
| **Total**  | **46** |

## Problems

| # | Problem | Difficulty | Pattern | Time | Space |
|---|---------|------------|---------|------|-------|
| 1 | [Two Sum](1_two_sum/) | Easy | Hash map | O(n) | O(n) |
| 54 | [Spiral Matrix](54_spiral_matrix/) | Medium | Boundary shrinking | O(m×n) | O(1) |
| 56 | [Merge Intervals](56_merge_intervals/) | Medium | Sort + greedy | O(n log n) | O(n) |
| 57 | [Insert Interval](57_insert_intervals/) | Medium | Three-case single pass | O(n) | O(n) |
| 62 | [Unique Paths](62_unique_paths/) | Medium | Dynamic programming (bottom-up) | O(m×n) | O(m×n) |
| 70 | [Climbing Stairs](70_climbing_stairs/) | Easy | Dynamic programming (Fibonacci) | O(n) | O(n) |
| 75 | [Sort Colors](75_sort_colours/) | Medium | Dutch National Flag (3 pointers) | O(n) | O(1) |
| 76 | [Minimum Window Substring](76_minimum_window_substring/) | Hard | Variable sliding window | O(n) | O(n) |
| 78 | [Subsets](78_subsets/) | Medium | Backtracking | O(2^n) | O(n) |
| 79 | [Word Search](79_word_search/) | Medium | DFS + Backtracking | O(m×n×4^L) | O(L) |
| 84 | [Largest Rectangle in Histogram](84_largest_rectangle_in_histogram/) | Hard | Monotonic stack | O(n) | O(n) |
| 98 | [Validate Binary Search Tree](98_validate_binary_search_tree/) | Medium | DFS with bounds | O(n) | O(n) |
| 102 | [Binary Tree Level Order Traversal](102_binary_tree_level_order_traversal/) | Medium | BFS level order | O(n) | O(n) |
| 104 | [Maximum Depth of Binary Tree](104_maximum_depth_of_binary_tree/) | Easy | DFS recursion | O(n) | O(n) |
| 105 | [Construct Binary Tree from Preorder and Inorder](105_construct_binary_tree_from_preorder_and_inorder_traversal/) | Medium | Divide and conquer | O(n) | O(n) |
| 110 | [Balanced Binary Tree](110_balanced_binary_tree/) | Easy | DFS with sentinel | O(n) | O(n) |
| 121 | [Best Time to Buy and Sell Stock](121_best_time_to_buy_and_sell_stock/) | Easy | Greedy / sliding min | O(n) | O(1) |
| 125 | [Valid Palindrome](125_valid_palindrome/) | Easy | Two pointers / regex | O(n) | O(n) |
| 127 | [Word Ladder](127_word_ladder/) | Hard | BFS | O(n×m×26) | O(n) |
| 199 | [Binary Tree Right Side View](199_binary_tree_right_side_view/) | Medium | BFS level order | O(n) | O(n) |
| 200 | [Number of Islands](200_number_of_islands/) | Medium | DFS flood fill | O(m×n) | O(m×n) |
| 206 | [Reverse Linked List](206_reverse_linked_list/) | Easy | Iterative three pointers | O(n) | O(1) |
| 207 | [Course Schedule](207_course_schedule/) | Medium | Topological sort (Kahn's) | O(V+E) | O(V+E) |
| 208 | [Implement Trie](208_implement_trie/) | Medium | Trie (prefix tree) | O(n) | O(n) |
| 217 | [Contains Duplicate](217_contains_duplicate/) | Easy | Hash set | O(n) | O(n) |
| 224 | [Basic Calculator](224_basic_calculator/) | Hard | Stack + sign tracking | O(n) | O(n) |
| 226 | [Invert Binary Tree](226_invert_binary_tree/) | Easy | DFS recursion | O(n) | O(n) |
| 230 | [Kth Smallest Element in BST](230_kth_smallest_element_in_bst/) | Medium | In-order traversal | O(n) | O(n) |
| 232 | [Implement Queue using Stacks](232_implement_queue_using_stacks/) | Easy | Two stacks | O(1) amortized | O(n) |
| 235 | [Lowest Common Ancestor of BST](235_LCA_of_a_binary_search_tree/) | Easy | BST navigation | O(n) | O(n) |
| 236 | [Lowest Common Ancestor of Binary Tree](236_LCA_of_a_binary_tree/) | Medium | DFS post-order | O(n) | O(n) |
| 238 | [Product of Array Except Self](238_product_of_array_except_self/) | Medium | Prefix + suffix products | O(n) | O(n) |
| 242 | [Valid Anagram](242_valid_anagram/) | Easy | Hash map (Counter) | O(n) | O(n) |
| 310 | [Minimum Height Trees](310_minimum_height_trees/) | Medium | Leaf trimming / BFS | O(n) | O(n) |
| 322 | [Coin Change](322_coin_change/) | Medium | Dynamic programming (tabulation) | O(n×m) | O(n) |
| 438 | [Find All Anagrams in a String](432_find_all_anagrams_in_a_string/) | Medium | Sliding window | O(n) | O(1) |
| 621 | [Task Scheduler](621_task_scheduler/) | Medium | Greedy + counting | O(n) | O(1) |
| 721 | [Accounts Merge](721_accounts_merge/) | Medium | Union-Find (DSU) | O(n log n) | O(n) |
| 733 | [Flood Fill](733_flood_fill/) | Easy | DFS in-place | O(m×n) | O(m×n) |
| 973 | [K Closest Points to Origin](973_k_closest_points_to_origin/) | Medium | Sort by distance | O(n log n) | O(1) |
| 1235 | [Maximum Profit in Job Scheduling](1235_maximum_profit_in_job_scheduling/) | Hard | DP + Binary search | O(n log n) | O(n) |
| 1848 | [Minimum Distance to the Target Element](1848_minimum_distance_to_the_target_element/) | Easy | Linear scan | O(n) | O(1) |
| 2515 | [Shortest Distance to Target String in a Circular Array](2515_shortest_distance_to_target_string_in_a_circular_array/) | Easy | Linear scan + circular distance | O(n) | O(1) |
| 3488 | [Closest Equal Element Queries](3488_closest_equal_element_queries/) | Medium | Hash map + binary search | O(n log n) | O(n) |
| 1855 | [Maximum Distance Between a Pair of Values](1855_Maximum_Distance_Between_a_Pair_of_Values/) | Medium | Binary search on negated array | O(n log n) | O(n) |
| 3761 | [Minimum Absolute Distance Between Mirror Pairs](3761_minimum_absolute_distance_between_mirror_pairs/) | Medium | Hash map + binary search | O(n log n) | O(n) |
