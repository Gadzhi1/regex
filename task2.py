import re

phrase = 'Always do your best. Your best is going to change from moment to moment;' \
         'it will be different when you are healthy as opposed to sick. ' \
         'Under any circumstance, simply do your best, and you will avoid self-judgment,' \
         'self-abuse and regret.'

while True:
    try:
        print('Press 0 to stop')
        x = int(input())

        if x > 0:
            word = str(input())

            count_word = len(re.findall(word, phrase))
            len_word = len(word)

            if count_word and len_word > 1:
                print(f'{count_word} слов в тексте')
                print(f'{len_word} букв в слове')

            else:
                print(f'{count_word} слово в тексте')
                print(f'{len_word} буква в слове')

        else:
            print('stop...')
            break

    except ValueError:
        print('ValueError! Try again')
