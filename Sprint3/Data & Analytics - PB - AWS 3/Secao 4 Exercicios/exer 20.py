a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]

reversed_a = list(reversed(a))
reversed_a_str = list(map(str, reversed_a))
result = "[" + ", ".join(reversed_a_str) + "]"

print(result)