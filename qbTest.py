#The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.
import math


#----necesary functions----
#Function that makes version string into a string of numbers.For now keep them as string in order to know their length

def getNumber(string):
    val = (string.replace('.',''))
    return val

#Function that takes number strings, casts them to integer values with the same number of digits. This way their values can be compared. Example, 3.0 is greater than 2.9.9.9 because 3000 is greater than 2999.
def getComparable(x, factor):
    exp = (factor - len(x)) #power of 10 needed to get numbers with equal number of digits
    val = ((int(x))*(math.pow(10,exp)))
    return val

def getMostRecent(string1, string2):
    #get versions as string of numbers
    val1 = getNumber(string1)
    val2 = getNumber(string2)
    
    #get the number of digits both numbers need to be to compare their value
    eF = max(len(val1), len(val2))

        #compare integer values (with same number of digits). The greater value is the greater or most recent version.
    if((getComparable(val1, eF)>getComparable(val2, eF))):
        return(string1+ " is greater than "+string2)
    
    elif((getComparable(val1, eF)<getComparable(val2, eF))):
        return(string2+" is greater than "+string1)
    else:
        return(string2+" and "+string1+ " are the same version!")
