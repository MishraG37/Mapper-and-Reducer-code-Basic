#!/usr/bin/env python

# import sys because we need to read and write data to STDIN and STDOUT
import sys

# reading entire line from STDIN (standard input)
for line in sys.stdin:
	# to remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	words = line.split()
	
	# we are looping over the words array and printing the word
	# with the count of 1 to the STDOUT
	for word in words:
		# write the results to STDOUT (standard output);
		# what we output here will be the input for the
		# Reduce step, i.e. the input for reducer.py
		print '%s\t%s' % (word, 1)                       (%s means print string ) (\t means give a tab distance)

==============================================================================================================================================================================
		
		
		
		
		i.e. let input of map code  is 
		the quick quick brown fox jumped jumped
		
		then due to strip(removed the spaces) and splitted into List
		words =['the', 'quick', 'quick', 'brown', 'fox', 'jumped', 'jumped']
		
		
		and now we are printing each word,1
		i.e.
		
		
		the 1
		quick 1
		quick 1     ===========> So this is the output of mapper.py and will be now given to reducer.py
		brown 1 
		fox 1
		jumped 1
		jumped 1
		 
