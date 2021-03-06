# hw9-Dunn.py
# Derrell Dunn

from datetime import datetime
from datetime import timedelta

def search_list(dict_list, value):
    # Brute force search for 'value' in the list 'L'
    # by examining entries one at a time until it's found
    # or the list has been exhausted.
    for index in range(len(dict_list)):
        if dict_list[index] == value:
            found_index = index
            break
    else:
        found_index = -1

    return found_index


def bsearch_list(dict_list, value):
    # Search for 'value' in the sorted list 'L' using a binary
    # search. COMPLETE the code that's here; 
    # DO NOT just ignore or delete or change this code, but actually complete
    # it as outlined in the presentation. 
    lower_bound = 0
    upper_bound = len(dict_list)-1
    while lower_bound <= upper_bound and (abs(lower_bound - upper_bound) >= 1):
        pivot_point = (lower_bound+upper_bound)/2
        if (dict_list[pivot_point] < value) and (abs(lower_bound - upper_bound) > 1):
            lower_bound = pivot_point
            continue
        elif dict_list[pivot_point] > value and (abs(lower_bound - upper_bound) > 1):
             upper_bound = pivot_point
             continue
        elif (dict_list[pivot_point] == value):
            return pivot_point
            break
        elif  (dict_list[pivot_point+1] == value):
            return pivot_point + 1
            break
        else:
            return -1
            break

    return -1


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
    print "!!!Brute force search did NOT find %s in the list (took %f seconds)!!!"%(val, duration.total_seconds())


##################################
##### Time the binary search #####
##################################

start = datetime.now()
index = bsearch_list(L, val)
stop = datetime.now()
duration = stop-start
if ((index >= 0) and (index < len(L)) and (L[index] == val)):
    print 'Binary search found it in %1.20f seconds.' % (duration.total_seconds())
    print 'Found it!! {} at index {}'.format(L[index], index)
else:
    print '!!!Binary search did NOT find %s in the list (took %f seconds)!!!' % (val, duration.total_seconds())



