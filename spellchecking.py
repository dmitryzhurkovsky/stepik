spellcheking = set()
words_count = int(input())
printed = set()
for i in range(words_count):
    spellcheking.add(input().lower())

test_text_count = int(input())
for line in range(test_text_count):
    text = input()
    for i in text.lower().split():
        if i not in spellcheking and i not in printed:
            print(i)
            printed.add(i)
