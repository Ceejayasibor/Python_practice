def rotate(word, number):
    letter = 'abcdefghijklmnopqrstuvwxyz'
    new_word = ''

    for char in word:
        i = letter.index(char)
        j = (i + number) % 26
        new_word += letter[j]
    return new_word

word = 'chill'
number = 7

print(rotate(word, number))


if __name__ == '__main__':
    print(rotate('cheer', 7))
    print(rotate('melon', -10))
    print(rotate('sleep', 9))
