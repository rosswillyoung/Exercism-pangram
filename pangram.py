def is_pangram(sentence):
    alphabet = list('qwertyuiopasdfghjklzxcvbnm')
    lowerSen = list(sentence.lower())

    for i in alphabet:
        if i not in lowerSen:
            return False
    return True

