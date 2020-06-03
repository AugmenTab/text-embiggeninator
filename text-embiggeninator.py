import sys, pyperclip, eel

eel.init('web')

@eel.expose
def embiggeninate_text(data):
    embiggeninated = []
    for character in data.lower():
        if character.isalpha():
            embiggeninated.append(':regional_indicator_' + character + ':')
        elif character == '!':
            embiggeninated.append(':exclamation:')
        elif character == '?':
            embiggeninated.append(':question:')
        elif character.isspace():
            embiggeninated.append('    ')
        else:
            embiggeninated.append(character)
    paste = ' '.join(embiggeninated)
    pyperclip.copy(paste)
    return paste

eel.start('index.html', size=(1000,600))