# Py-Blind
A little script that generates blinds and renames files in a data directory to help blind analysis.
I made this for my own use while analyzing images in wet lab.

Written for Python 2.7.8 on OSX 10.10.1

Feel free to modify for your own use! Licensed under the MIT license.

##Usage
Place the two scripts "blind.py" and "unblind.py" in the directory containing *a copy* of your data files.
Begin at the command line:

$ python blind.py

and answer the prompts that follow.
**Make sure that your labels are not substrings of other labels. For example, using the labels "NONE" and "NONE_EXTRA" would result in erroneous blinding.**
The script will ask you to confirm before renaming files.

When you're ready, view the blind mapping by opening the generated "blinds.txt" file.
To unblind, leave "blinds.txt" in the folder and at the command line:

$ python unblind.py

After that, everything should be back as it started!
