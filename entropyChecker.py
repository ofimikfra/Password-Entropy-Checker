import math, re

def readPassword(password):
    lower, upper, num, symbol = False, False, False, False
    n = 0 # password space
    symbols = re.compile(r"[!@#$%^&*()-+_=:;,./?{}\[\]'\"~`\\<>|]")
    doesNotContain = []

    for c in password:
        if c.islower() and not lower:
            n += 26
            lower = True
        elif c.isupper() and not upper:
            n += 26
            upper = True
        elif c.isdigit() and not num:
            n += 10
            num = True
        elif re.search(symbols, c) and not symbol:
            n += 32
            symbol = True

    if not lower:
        doesNotContain.append("lowercase letters")
    if not upper:
        doesNotContain.append("uppercase letters")
    if not num:
        doesNotContain.append("numbers")
    if not symbol:
        doesNotContain.append("symbols")

    length = len(password)
    
    return n, doesNotContain, length

def calculateEntropy(n, dnc, length):
    # E = log2(N)
    entropy = math.log2(n**length)

    if entropy >= 90:
        print(f"Your password's entropy is high: {round(entropy,3)} bits. You have a strong password!")

    elif entropy >= 75:
        print(f"Your password's entropy is high: {round(entropy,3)} bits. You have a good password!")

    else:
        if entropy >= 65:
            print(f"Your password's entropy is average: {round(entropy,3)} bits. You have an okay password, but it could be better!")

        elif entropy >= 50:
            print(f"Your password's entropy is low: {round(entropy,3)} bits. You have a weak password.")
        
        else:
            print(f"Your password's entropy is too low: {round(entropy,3)} bits. You have a poor password.")

        if dnc:
            suggestion = "Try adding "

            for i in range(len(dnc)):
                suggestion += dnc[i]

                if len(dnc) != 2:
                    if i < len(dnc) - 2:
                        suggestion += ", "
                    elif i == len(dnc) - 2:
                        suggestion += ", and "
                else:
                    suggestion += " and "

            suggestion += " to your password to make it stronger."

            print(suggestion)

        else:
            print("Try making a longer password (more than 8 characters).")
            print(f"Current password length: {length}")
            
