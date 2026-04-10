from solution import Trie

trie = Trie()
trie.insert("apple")
trie.insert("app")

tests = [
    ("search",     "apple", True),
    ("search",     "app",   True),
    ("search",     "ap",    False),
    ("startsWith", "app",   True),
    ("startsWith", "b",     False),
]

for action, arg, expected in tests:
    got = getattr(trie, action)(arg)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | {action}({arg}) | got={got} | expected={expected}")
