import re
import os
import io
import codecs

def function(items):
    result = []
    for item in items:
        result.append(f'item: {item}')
    return result


for i in function(range(4)):
    print(i)
print("\n")


def yield_function(items1):
    for item1 in items1:
        yield f'item1: {item1}'


for x in yield_function(range(4)):
    print(x)


mail_log = ['Jun 18 14:10:35 client-ip=154.10.180.10 from=user1@gmail.com, size=551',
            'Jun 18 14:11:05 client-ip=150.10.180.10 from=user2.test@gmail.com, size=768']

for message in mail_log:
    match = re.search(r'\w+\.?\w+@\w+\.\w+', message)
    if match:
        print("Found email: ", match.group())

print(os.getcwd())

file = open('ignes.txt', 'r+', encoding='utf-8', errors='ignore')
print(file.read())

file.seek(0)
print(file.read())

pattern = r'\d{4}'

for line in open("ignes.txt", errors='replace' ):
    match = re.search(pattern, line).group()
    print(match)
