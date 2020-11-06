count = 0
s = input()
a = input()
b = input()
while "a" in "s":
    count =+ 1
    s.replace("a", "b")
    if count >= 1000:
        print("Impossible")
        break
    else:
        print(count)