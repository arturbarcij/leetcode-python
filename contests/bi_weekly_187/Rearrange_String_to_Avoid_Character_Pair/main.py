from solution import Solution

solution = Solution()


def has_forbidden_pair(c, x, y):
    """True if some x appears before some y (subsequence, not just adjacent)."""
    return x in c and y in c and c.index(x) < c.rindex(y)


# The problem accepts ANY valid rearrangement, so validate properties
# rather than matching one exact string. (x != y is guaranteed.)
tests = [
    ("aabc", "a", "c"),
    ("dcab", "d", "b"),
    ("axe", "o", "x"),
    ("ab", "a", "b"),
    ("abab", "a", "b"),
    ("zzz", "a", "b"),
    ("a", "a", "b"),
]

for s, x, y in tests:
    got = solution.rearrangeString(s, x, y)

    is_rearrangement = sorted(got) == sorted(s)
    avoids = not has_forbidden_pair(got, x, y)
    ok = is_rearrangement and avoids

    reason = ""
    if not is_rearrangement:
        reason = " (not a rearrangement of s)"
    elif not avoids:
        reason = f" ('{x}' appears before '{y}')"

    status = "PASS" if ok else "FAIL"
    print(f"{status} | s={s} x={x} y={y} | got={got!r}{reason}")
