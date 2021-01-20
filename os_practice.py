import os

result = set()
for current_dir, dirs, files in os.walk('main'):
    for data in files:
        if data.endswith('.py'):
            result.add(current_dir)

result = '\n'.join(list(sorted(result)))
with open('main_result.txt', 'w') as outfile:
    outfile.write(result)