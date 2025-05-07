#!/usr/bin/env python3

from entropyChecker import readPassword, calculateEntropy

while True:
    
    password = input("\nEnter your password (or press enter to quit): ")

    if password != "":
        n, dnc, len = readPassword(password)
        calculateEntropy(n, dnc, len)
    else:
        break
