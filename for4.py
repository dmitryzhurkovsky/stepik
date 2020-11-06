count = 0
s = str(input())
t = str(input())
for i in range(0, len(s)):
    tmp = s[i:].startswith(t)
    if tmp is True:
        count += 1
print(count)
