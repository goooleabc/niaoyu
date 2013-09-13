# Here is some comments.
# author: goooleabc
# date 	: 2013.09.13
# functions:
#	some specifications
#
'''You can write some comments here, too.'''

# the usage of doma
dna = "ATCGATCG"
dna2 = "ACCCAGGG"
print "First and Second sequences\n"
print dna, dna2

# the usage of plus
dna3 = dna + dna2
print "Concatenated sequence\n"
print dna3

print "dna + dna2:[",(dna + dna2),"]\n"

'''This section shows how to import a module 
and use the regex module to transcribe DNA TO RNA.
'''
# the usage of regular expression
# import the regular expression module
import re
## assigning a new regex and compiling it to find all Ts
regexp = re.compile('T')
## create a new string to receive the regexp result with Us replacing Ts
rna = regexp.sub('U', dna)
print "dna:",dna," || rna:",rna


'''Open a file and print all lines'''
## assigning  a filename to a variable
file_in = "..\\README.md"
## opening the file
file = open(file_in,'r')
## printing each line of the file
print "Lines in",file_in,"\n"
for line in file:
    ## note the comma here. print "\n" here if no comma.
    print line,




