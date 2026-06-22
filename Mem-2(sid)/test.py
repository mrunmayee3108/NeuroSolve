from guardrail_sandbox import execute_with_guardrails

# Test 1 — correct code
code1 = "result = 10 - 5"
answer, status = execute_with_guardrails(code1)
print(f"Test 1: answer={answer}, status={status}")
# Expected: answer=5, status=Success

# Test 2 — logic violation (assert fails)
code2 = """
result = 10 + 5
assert result < 10, "Final apples must be less than starting apples!"
"""
answer, status = execute_with_guardrails(code2)
print(f"Test 2: answer={answer}, status={status}")
# Expected: answer=None, status=LOGIC VIOLATION: ...

# Test 3 — undefined variable
code3 = "result = apples - 5"
answer, status = execute_with_guardrails(code3)
print(f"Test 3: answer={answer}, status={status}")
# Expected: answer=None, status=VARIABLE ERROR: ...

# Test 4 — syntax error
code4 = "result = 10 +* 5"
answer, status = execute_with_guardrails(code4)
print(f"Test 4: answer={answer}, status={status}")
# Expected: answer=None, status=SYNTAX CRASH: ...
