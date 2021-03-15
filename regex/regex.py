import re

pattern = r'sorry'
i = 1
with open('ignes.txt', 'r+', encoding='utf-8', errors='ignore') as file1:
    print(file1.read())
    file1.seek(0)
    for line in file1:
        match = re.search(pattern, line)
        if match:
            print(f'Match {i}:', match.group())
            i += 1
