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

<<<<<<< HEAD
userlist = input('Enter your List separated by a comma:\n')
=======
userlist = raw_input('Enter your List separated by a comma:\n')
>>>>>>> 255c6bdcfe0c98df0803052d01ce327a1c30384d

#Convert user input to a list
listitems = userlist.split(',')

<<<<<<< HEAD
print("Your list is: ", listitems)

print(sorted(listitems))
=======
print"Your items are: ",listitems
# to sort the list
sorteditems=sorted(listitems)
print"Your sorted items are: ",sorteditems
>>>>>>> 255c6bdcfe0c98df0803052d01ce327a1c30384d
