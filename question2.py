""" Question Two

Design and implement an algorithm that takes: a list containing n distinct natural numbers and a number k ≤ n and
calculates the sum of the k largest numbers in the array. For example, if the list is {3, 7, 5, 12, 6} and k = 3, then
the algorithm should return 25= (12+7+6).

Implement the algorithm in python [5] """


# Defining the function to the couunting of the elements in the list
def largestNumber(n, k):
    # Creating a variable to store the list after removing duplicates by using the set
    DistinctList = list(set(n))
    # if the k passed is the less than the number of elements in the distinct list
    if k <= len(DistinctList):
        # We show the list
        print(f"\nThe distinct list: {DistinctList}")
        # and sort in descending order do that we can perform operations easily on the largest largest element
        # (first elements)
        newList = sorted(DistinctList, reverse=True)
        return f"The sum of {k} largest numbers is: {sum(newList[:k])}"


print(largestNumber([10, 6, 7, 10, 10, 1, 8, 1,], 3))

