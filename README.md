# Py-Blind
A little script that generates blinds and renames files in a data directory to help blind analysis.
I made this for my own use while analyzing images in wet lab.

Written for Python 2.7.8 on OSX 10.10.1

Feel free to modify for your own use! Licensed under the MIT license.

##Usage
At the command line:

$ python blind.py

and answer the prompts that follow.
It will ask you to confirm before renaming files.

**Make sure that your labels are not substrings of other labels. i.e. "NONE" and "NONE_EXTRA" would result in erroneous blinding**
