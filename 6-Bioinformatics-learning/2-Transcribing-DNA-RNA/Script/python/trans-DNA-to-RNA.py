## Read the sequence from the file ##

import sys

pathOfInputFile = sys.argv[1]
print(pathOfInputFile)
pathOfOutputFile = sys.argv[2]
print(pathOfOutputFile)

inputFile = open(pathOfInputFile, 'r')
dnaSeq = inputFile.readline().strip('\n')
inputFile.close()

## Replace T with U ##
rnaSeq = dnaSeq.replace("T","U")

## Print the Output of the counts ##
print(
'''The RNA sequence of DNA {1} is given below:
-----------------------
-  {0}                -
-----------------------'''.format(rnaSeq, dnaSeq))

## Save the Output in a csv file format ##
outputFile = open(pathOfOutputFile, 'w')
outputFile.write(
"DNASeq,RNASeq\n"
"{1},{0}".format(rnaSeq, dnaSeq))
outputFile.close()

## Give update that the file is saved ##
print('The output file is saved in the location {0}'.format(pathOfOutputFile))
