import math, re

def readPassword(password):
    n, lower, upper, num, symbol = 1,1,1,1,1
    symbols = re.compile(r"[!@#$%^&*()-+_=:;,./?{}\[\]'\"~`\\<>|]")
    doesNotContain = []

    for c in password:
        if c.islower():
            lower *= 26**1
            print(c, "lower")
        elif c.isupper():
            upper *= 26**1
            print(c, "upper")
        elif c.isdigit():
            num *= 10**1
            print(c, "num")
        elif re.search(symbols, c):
            symbol *= 32**1
            print(c, "symbol")

    print(lower, upper, num, symbol)

    if lower == 1:
        doesNotContain.append("lowercase letters")
    if upper == 1:
        doesNotContain.append("uppercase letters")
    if num == 1:
        doesNotContain.append("numbers")
    if symbol == 1:
        doesNotContain.append("symbols")

    length = len(password)

    # N = password space
    for i in [lower, upper, num, symbol]:
        if i > 1:
            print(n, "+", i, "=", n*i)
            n *= i

    print(n)
    
    return n, doesNotContain, length

def calculateEntropy(n, dnc, length):
    # E = log2(N)
    entropy = math.log2(n)

    if entropy >= 75:
        print(f"Your password's entropy is high: {round(entropy,3)} bits. You have a strong password!")

    if entropy >= 50:
        print(f"Your password's entropy is average: {round(entropy,3)} bits. You have a good password!")

    else:
        if entropy >= 25:
            print(f"Your password's entropy is low: {round(entropy,3)} bits. You have a weak password.")
        
        else:
            print(f"Your password's entropy is too low: {round(entropy,3)} bits. You have a poor password.")

        if dnc:
            suggestion = "Try adding "

            for i in range(len(dnc)):

                if i > len(dnc)-1:
                    suggestion += ", and "

                suggestion += dnc[i]

                if i < len(dnc)-1:
                    suggestion += ", "

            suggestion += " to your password to make it stronger."

            print(suggestion)

        else:
            print("Try making a longer password (around 8-31 characters).")
            print(f"Current password length: {length}")
            
