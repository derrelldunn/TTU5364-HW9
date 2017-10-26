# hw9-Dunn.py
# Derrell Dunn
from datetime import datetime
from datetime import timedelta

def search_list(L, value):
    # Brute force search for 'value' in the list 'L'
    # by examining entries one at a time until it's found
    # or the list has been exhausted.
    pass

def bsearch_list(List, value):
    # Search for 'value' in the sorted list 'L' using a binary
    # search. COMPLETE the code that's here; 
    # DO NOT just ignore or delete or change this code, but actually complete
    # it as outlined in the presentation. 
    L = 0
    U = len(List)-1
    while (L<=U): 
      pass


###################################################
####### Do not change anything below here!! #######
###################################################
def read_list_from_file(filename):
    L = []
    try:
        F = open(filename, "r")
    except:
        print "Could not open file '%s'!" % (filename)
        return []
    for line in F:
        L.append(line.strip())
        
    return L


######################################
########## Execution point ###########
######################################
inputfile="input.txt"
L = read_list_from_file(inputfile)
print "Read %d items from file '%s'" % (len(L), inputfile)
val = raw_input('Enter a value to search for: ')

########################################
##### Time the brute force search: #####
########################################
start = datetime.now()
index = search_list(L, val)
stop = datetime.now()
duration = stop-start
if ((index >=0) and (index < len(L)) and (L[index]==val)):
    print "Brute force search found it in %f seconds."%(duration.total_seconds())
else:
    print "Brute force search did not find %s in the list (took %f seconds)."%(val, duration.total_seconds())

##################################
##### Time the binary search #####
##################################
start = datetime.now()
index = bsearch_list(L, val)
stop = datetime.now()
duration = stop-start
if ((index >=0) and (index < len(L)) and (L[index]==val)):
    print "Binary search found it in %f seconds."%(duration.total_seconds())
else:
    print "Binary search did not find %s in the list (took %f seconds)."%(val, duration.total_seconds())


