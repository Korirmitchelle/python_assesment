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
<<<<<<< HEAD
userlist = raw_input('Enter your List separated by a comma:\n')
=======
userlist = input('Enter your List separated by a comma:\n')
>>>>>>> 5e4fb5ef7dbf9edd02d007b46cc4dceb60265dab
=======
userlist = input('Enter your List separated by a comma:\n')
=======
userlist = raw_input('Enter your List separated by a comma:\n')
>>>>>>> 255c6bdcfe0c98df0803052d01ce327a1c30384d
>>>>>>> dc0804395e97bc7c392821f0dcaa6b6ad8d22846

#Convert user input to a list
listitems = userlist.split(',')

<<<<<<< HEAD
<<<<<<< HEAD
=======
print("Your list is: ", listitems)

print(sorted(listitems))
=======
>>>>>>> dc0804395e97bc7c392821f0dcaa6b6ad8d22846
print"Your items are: ",listitems
# to sort the list
sorteditems=sorted(listitems)
print"Your sorted items are: ",sorteditems
<<<<<<< HEAD
=======
print("Your list is: ", listitems)

print(sorted(listitems))
>>>>>>> 5e4fb5ef7dbf9edd02d007b46cc4dceb60265dab
=======
>>>>>>> 255c6bdcfe0c98df0803052d01ce327a1c30384d
>>>>>>> dc0804395e97bc7c392821f0dcaa6b6ad8d22846
