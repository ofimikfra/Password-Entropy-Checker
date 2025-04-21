import math, re

def readPassword(password):
    possibleCharacters = 0
    lower, upper, num, symbol = False, False, False, False
    symbols = re.compile(r"['\"@_!#$%^&*()<>?/\\|}{~:]")

    for c in password:
        if c.islower() and not lower:
            possibleCharacters += 26
            lower = True
        elif c.isupper() and not upper:
            possibleCharacters += 26
            upper = True
        elif c.isdigit() and not num:
            possibleCharacters += 10
            num = True
        elif re.search(symbols, c) and not symbol:
            possibleCharacters += 32
            symbol = True

    length = len(password)
    return length, possibleCharacters

def calculateEntropy(length, possibleCharacters):
    entropy = math.log2(possibleCharacters**length)
