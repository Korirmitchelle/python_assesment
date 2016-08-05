"""
Question: 1

Write a program that accepts a comma separated sequence of words as input and
prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
    without,hello,bag,world
Then, the output should be:
    bag,hello,without,world

Hints: In case of input data being supplied to the question, it should be
assumed to be a console input. Use a sorting method

"""



#Get user input.

userlist = raw_input('Enter your List separated by a comma:\n')

#Convert user input to a list
listitems = userlist.split(',')

print"Your items are: ",listitems
# to sort the list
sorteditems=sorted(listitems)
print"Your sorted items are: ",sorteditems
