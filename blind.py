#script to blind
import os
import random

labels = ["NM48", "NM-ZV-MT", "NM-MT", "NM-ZV", "NPM"]
blinds = ["A", "B", "C", "D", "E"]

random.shuffle(blinds)
bmap = {}

for i in range(len(labels)):
	bmap[labels[i]] = blinds[i]

for filename in os.listdir("."):
	if filename[-3:] == "tif": # if the file is a tif file (excludes our own files)
		newfilename = filename.replace(filename[16:filename.index("_")], bmap[filename[16:filename.index("_")]])
	os.rename(filename, newfilename)

f = open('blinds.txt','w')

for x in range(len(labels)):
    f.write(labels[x] + ": " + blinds[x] + "\n")

f.close()
