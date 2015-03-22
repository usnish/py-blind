#script to unblind
#python 2.7.8
import os

#helper function for confirmation
def confirm(question):
	while True:
		answer = raw_input(question)
		if answer not in ['y', 'Y', 'n', 'N']:
			print 'please enter y or n.'
			continue
		if answer == 'y' or answer == 'Y':
			return True
		if answer == "n" or answer == 'N':
			return False

#variables
blindmap = {}

###########################

f = open('blinds.txt','r')
for line in f.readlines(): # read blinds from file
    parsed = line.strip().split(',')
    print "Reading blind: ",
    print parsed
    blindmap[parsed[0]] = parsed[1] # parsed [0] is the key filename element, [1] is the blind

f.close()


# switch filenames back
if confirm("Ready to change filenames back. Do you wish to continue? Make sure you're working with a *copy* of your data. [y/n]: "):
	print "UN-Blinding filenames..."
	for filename in os.listdir("."):
		newfilename = filename
		for x in blindmap:
                        if blindmap[x] in filename:
                                newfilename = filename.replace(blindmap[x], x) # note switched order relative to blind.py
		os.rename(filename, newfilename)
		print filename + " processed."
	print "All done!"
else:
	print "Operation canceled. Quitting!"
