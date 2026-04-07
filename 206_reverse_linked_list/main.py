from solution import Solution, ListNode


def make_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


s = Solution()

tests = [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([1, 2],          [2, 1]),
    ([],              []),
]

for values, expected in tests:
    got = to_list(s.reverseList(make_list(values)))
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | input={values} | got={got} | expected={expected}")
