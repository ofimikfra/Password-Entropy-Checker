# Password-Entropy-Checker
Part 1 of CSCI262 Project

## How to Run the Program
> Make sure Python is installed on your device.
1. Clone or download this repository onto your local machine.
2. Navigate to the repository and run the command `python main.py`.

> Alternatively, you can execute the "passwordEntropyCheckr" .exe file located in the "dist" directory.

## What Users Should Expect
Upon running the program, it will prompt you to enter a password. Once entered, the program will calculate the entropy using the password entropy formula (`log2(N^L)`, where N is the password space and L is the length of the password). The program determines the strength of the password along with the result and gives suggestions on how to make the password stronger. 

Password strength is based on the following:
- 90 and above: Strong
- 75 to 89: Good
- 65 to 74: Average
- 50 to 64: Low
- Less than 50: Poor