from entropyChecker import readPassword, calculateEntropy

password = input("Enter your password: ")

n, dnc, len = readPassword(password)
calculateEntropy(n, dnc, len)
