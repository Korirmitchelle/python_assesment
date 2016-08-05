"""

Question: 2

Write a program that accepts sequence of lines as input and prints the lines
after making all characters in the sentence capitalized. Suppose the following
input is supplied to the program:
    Hello world Practice makes perfect
Then, the output should be:
    HELLO WORLD PRACTICE MAKES PERFECT

Hints: In case of input data being supplied to the question,
it should be assumed to be a console input. Use list and append

"""

print("Enter your Lines. Please press 1 to submit:\n")

userlines = []

terminate = '1'

for line in iter(raw_input, terminate):
    userlines.append(line.upper())
    pass
for item in userlines:
    print(item)
