#! python 3

import sys

def embiggeninateText(string):
    print(string)

while True:
    print('Enter some text to embiggeninate.')
    text = input()
    if text == 'q':
        print('Goodbye!')
        sys.exit(0)
    embiggeninateText(text)