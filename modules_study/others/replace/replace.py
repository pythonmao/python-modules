import os
import sys

usage = "usage: %s search_text replace_text [infilename [outfilename]]" % os.path.basename(
    sys.argv[0])

if len(sys.argv) != 5:
    print usage
else:
    rtext = sys.argv[1]
    xtext = sys.argv[2]

    rfile = open(sys.argv[3])
    xfile = open(sys.argv[4], "w")

    for text in rfile:
        xfile.write(text.replace(rtext, xtext))

    rfile.close()
    xfile.close()

