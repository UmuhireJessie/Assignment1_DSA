"""State the Big O-notation and implement the algorithm that perform the following operations:

The algorithm takes as input a list of numbers which may contain duplicates. It returns true if
all elements of the list occur an odd number of times. Otherwise it returns false. For example, on the
list {1, 3, 2, 2, 5, 2} it returns true, but on the list {1, 3, 2, 2, 5, 2, 5} it returns false because
5 occurs an even number of times. [5] """

import timeit
from collections import Counter
from matplotlib import pyplot as plt

# FIRST METHOD


# Defining a function to count the element in the list
def counting_odds(list_):
    # Creating a variable to store the time used to run the function
    startTime = timeit.timeit()
    # Creating a variable to store the counts of each element in the list using Counter module, the counter will be a
    # a dictionary where key are elements and values are counts of each element in the list
    counter = Counter(list_)
    # Initialising a count variable to count the values (of keys) which are odd
    count = 0
    for key in counter:
        if counter[key] % 2 != 0:
            count += 1
    # returning the result
    #return f'{True}, The time taken to run is: {startTime}' if count == len(set(list_)) else f'{True}, The time taken
    # to run is: {startTime}'
    return startTime


# SECOND METHOD

# Defining a function to count the element in the list
def countingDict(list_):
    # Creating a variable to store the time used to run the function
    ts = timeit.timeit()
    # Creating an empty dictionary that will be used to count
    count_dictionary = {}
    # Iterating through the list, making elements of the list the key to dictionary and values to be the counts
    for element in list_:
        if element in count_dictionary:
            count_dictionary[element] += 1
        else:
            count_dictionary[element] = 1
    # creating a variable count to count values which are odd
    count = 0
    for key in count_dictionary:
        if count_dictionary[key] % 2 != 0:
            count += 1
    # returning true if the count is equal to the len of set of the list and false otherwise (a set because it doesn't
    # allow duplicates, so we will see if all elements' values have been counted to be odd
    return f'{True}, The time taken to run is: {ts}' if count == len(set(list_)) else f'{False}, The time taken to run is: {ts}'


# Testing on the two lists from the prompt
list1 = [1, 3, 2, 2, 5, 5, 2]
list2 = [1, 3, 2, 2, 5, 2]

# Implementing the big O notation
L = []
list3 = range(1,1000)
for l in list2:
    lst = [1] * l
    ts = timeit.timeit()
    counting_odds(lst)
    L.append(ts)

plt.plot(list2, L, 'o-', label='change of time with length')
plt.xlabel('lengths of list')
plt.ylabel('Average time (ms)')
plt.show()

print(counting_odds(list2))
print(countingDict(list2))
print("\nThe Big O notation of the algorithm is O(n) ")  # not sure

