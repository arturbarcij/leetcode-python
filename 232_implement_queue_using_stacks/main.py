from solution import MyQueue

q = MyQueue()

tests = [
    ("push", 1, None),
    ("push", 2, None),
    ("peek", None, 1),
    ("pop", None, 1),
    ("empty", None, False),
    ("pop", None, 2),
    ("empty", None, True),
]

for op, arg, expected in tests:
    if op == "push":
        q.push(arg)
        print(f"PUSH {arg}")
    elif op == "pop":
        got = q.pop()
        status = "PASS" if got == expected else "FAIL"
        print(f"{status} | pop: got={got} | expected={expected}")
    elif op == "peek":
        got = q.peek()
        status = "PASS" if got == expected else "FAIL"
        print(f"{status} | peek: got={got} | expected={expected}")
    elif op == "empty":
        got = q.empty()
        status = "PASS" if got == expected else "FAIL"
        print(f"{status} | empty: got={got} | expected={expected}")
