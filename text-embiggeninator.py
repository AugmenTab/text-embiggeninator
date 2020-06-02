#! python 3

import sys, pyperclip

def embiggeninateText(string):
    embiggeninated = []
    for character in string:
        if character.isalpha():
            alpha = character.lower()
            embiggeninated.append(':regional_indicator_' + alpha + ':')
        elif character == '!':
            embiggeninated.append(':exclamation:')
        elif character == '?':
            embiggeninated.append(':question:')
        elif character.isspace():
            embiggeninated.append('    ')
        else:
            embiggeninated.append(character)
    pyperclip.copy(' '.join(embiggeninated))
    print('Ready for pasting!')

while True:
    print('Enter some text to embiggeninate, or enter q to quit.')
    text = input()
    if text == 'q':
        print('Goodbye!')
        sys.exit(0)
    embiggeninateText(text)