import re

n, m = map(int, input().split())
a, b = [], ""

for i in range(n):
    a.append(input())

for row in range(m):
    for column in range(n):
        b += a[column][row]
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))