word_1 = 'pots'
word_2 = 'stop'
def is_reverse(word_1, word_2):
    if len(word_1) != len(word_2):
        return False
    i = 0
    j = len(word_2) - 1
    while i < len(word_1):
        if word_1[i] != word_2[j]:
            return False
        i += 1
        j -= 1
    return True


result = is_reverse(word_1, word_2)
print(result)
