#!/usr/bin/env python

import os
import sys

if len(sys.argv) != 3:
  print("Wrong arguments!")
  print "Syntax:\n", os.path.basename(sys.argv[0]), "<file full path> <output file>"
  sys.exit()

input_line=sys.argv[1]
outfile=sys.argv[2]

outfh = open(outfile,"a+")
outfh.write("{}\n".format(input_line))

while True:
  input_line = os.path.dirname(input_line)
  outfh.write("{}\n".format(input_line))
  if(input_line == "/"):
    break

outfh.close()
