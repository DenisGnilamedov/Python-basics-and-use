def gimme_the_letters(letters):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    first = letters[0]
    last = letters[2]
    for letter in alphabet:
        if first <= letter <= last:
            print(letter, end='')
        else:
            continue





gimme_the_letters("G-T")