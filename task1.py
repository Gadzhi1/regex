names = ['John', 'Oscar', 'Jacob']

with open('names.txt', 'w+', encoding='utf-8') as f:
    for i in names:
        print(i)
        f.writelines(i+'\n')
    f.seek(0)
    f.read()
    f.close()

