"""
Question: 3

Write a program which accepts a sequence of comma separated 4 digit binary
numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated
sequence. Example:
    0100,0011,1010,1001
Then the output should be:
    1010 Notes:

Assume the data is input by console.

Hints: In case of input data being supplied to the question, it should be
assumed to be a console input. Use list and .join

"""

numbers = raw_input("Enter numbers to check separated by a comma:\n")

def isBinary(num):
    for i in range(len(num)):
        if int(num[i]) <= 1 and int(num[i]) >= 0:
            return True
        else:
            return False

numlist = numbers.split(',')
numberlist=[]
for num in numlist:
    if isBinary(num) and len(num) == 4:
        if int(num)%5==0:
            numberlist.append(num)

print(', '.join(numberlist))

