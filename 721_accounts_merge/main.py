from solution import Solution

s = Solution()

tests = [
    # Two John accounts share b@x.com → merged, Mary stays separate
    (
        [["John","a@x.com","b@x.com"],["John","c@x.com","b@x.com"],["Mary","d@x.com"]],
        [["John","a@x.com","b@x.com","c@x.com"],["Mary","d@x.com"]]
    ),
    # No shared emails → all accounts stay separate
    (
        [["Gabe","Gabe0@m.co","Gabe3@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co"],["Ethan","Ethan5@m.co"]],
        [["Ethan","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co"]]
    ),
]

for accounts, expected in tests:
    got = sorted(s.accountsMerge(accounts))
    status = "PASS" if got == sorted(expected) else "FAIL"
    print(f"{status} | got={got}")
