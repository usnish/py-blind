#script to blind
#python 2.7.8
import os
import random
from collections import OrderedDict

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

#Variables
labels = []
blindtext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
blinds = []
blindmap = {}

print "This script will generate blinds (A, B, C ...) for files in this folder."

#Asks for labels
while True:
	response = raw_input("Please enter label (portion of filename to blind), type 'done' if finished: ")
	if response == "done":
		print "Finished adding labels."
		break
	else:
		labels.append(response)
		labels = list(OrderedDict.fromkeys(labels)) # clean up duplicates in labels
		print "Labels: ",
		print labels

notfound = [] # list of items not found, for removal later
for label in labels: # looks for each label in filename
	found = 0
	for filename in os.listdir("."):
		if label in filename:
			print "Label '" + label + "' found!"
			found = 1
			break
	if found == 0:
		print "Label '" + label + "' not found."
		notfound.append(label)

for label in notfound: # remove those not found
	labels.remove(label)

print "Generating blinds for labels found: ",
print labels

for x in range(len(labels)): # initialize blinds as A, B, C, D, E, F...
	blinds.append(blindtext[x])

random.shuffle(blinds) # shuffle blinds

for i in range(len(labels)): # generate dict of labels and blinds
	blindmap[labels[i]] = blinds[i]

f = open('blinds.txt','w') # write blinds to file
for key in blindmap:
    f.write(key + "," + blindmap[key] + "\n")
f.close()

print "Blinds written to 'blinds.txt'. Look after you're done!"

if confirm("Ready to change filenames. Do you wish to continue? Make sure you're working with a *copy* of your data. [y/n]: "):
	print "Blinding filenames..."
	for filename in os.listdir("."):
		newfilename = filename
		for key in blindmap:
			newfilename = filename.replace(key, blindmap[key])
		os.rename(filename, newfilename)
		print filename + " processed."
	print "All done! Happy analysis!"
else:
	print "operation canceled. Quitting!"
