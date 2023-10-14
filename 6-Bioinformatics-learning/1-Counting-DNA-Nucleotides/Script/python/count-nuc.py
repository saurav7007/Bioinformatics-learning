## Read the sequence from the file ##

import sys

pathOfInputFile = sys.argv[1]
print(pathOfInputFile)
pathOfOutputFile = sys.argv[2]
print(pathOfOutputFile)

inputFile = open(pathOfInputFile, 'r')
seq = inputFile.readline().strip('\n')
inputFile.close()

## Loop to read count of each nucleotide ##
counts = {'A':0, 'T':0, 'G':0, 'C':0}

for nu,co in counts.items():
    co = seq.count(nu)
    counts[nu] = co

## Print the Output of the counts ##
print(
'''The count of each nucleotide for sequence {4} is as follows:
-----------------------
-  Count of A is {0}  -
-  Count of T is {1}  -
-  Count of G is {2}  -
-  Count of C is {3}  -
-----------------------'''.format(counts['A'], counts['T'], counts['G'], counts['C'], seq))

## Save the Output in a csv file format ##
outputFile = open(pathOfOutputFile, 'w')
outputFile.write(
"Seq,Count_of_A,Count_of_T,Count_of_G,Count_of_C\n"
"{4},{0},{1},{2},{3}".format(counts['A'], counts['T'], counts['G'], counts['C'], seq))
outputFile.close()

## Give update that the file is saved ##
print('The output file is saved in the location {0}'.format(pathOfOutputFile))
