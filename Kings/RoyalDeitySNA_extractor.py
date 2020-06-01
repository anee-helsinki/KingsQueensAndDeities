#!/usr/bin/python
# -*- coding: utf-8 -*-

import pmizer
import sys
import urllib.parse

# textfile to be analysed
inputfile = sys.argv[1]
# list of the words of interest
wanted = sys.argv[2]
# where to wrote
outputfile = sys.argv[3]
# size of the window, where co-orrurrences are looked for
window = int(sys.argv[4])

def readList(filename):
		words = list()
		with open(filename) as f:
			for line in f:
				words = [line.rstrip('\n') for line in open(filename)]
		return words



def doPMI(inputfile, words, outputfile, wsize):
		e = pmizer.Associations()
		e.set_window(size=wsize, symmetry=False)
		e.read_raw(inputfile)
		e.set_constraints(freq_threshold=1,
				freq_threshold_collocate=1,
				distance_scaling=False,
				words1=words,
				words2=words)
		e.score_bigrams(pmizer.PPMI2)
		e.print_scores(gephi=False)
		e.write_tsv(outputfile)



words = readList(wanted)
doPMI(inputfile, words, outputfile, window)
