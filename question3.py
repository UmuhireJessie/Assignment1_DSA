"""" KNAPSACK ALGORITHM """


"""Defining a function that will be used to implement the knapsack algorithm."""


def knapsack(list_of_values, list_of_weights, bag_capacity, number_of_pellets):
    """ I have first created a dummy kind of table that will have the range of the pellets as the rows starting from and
    the range of weights or the capacity a bag can be able to carry as the columns"""

    k = [[0 for _ in range(bag_capacity + 1)] for _ in range(number_of_pellets + 1)]

    """I created nested for loop to iterate through the ranges of the pellets (rows) and the bag capacity (columns) and 
    insert the values of the pellets as the capacity continues to change (to increased) based on the different 
    conditions."""
    for i in range(number_of_pellets + 1):
        for w in range(bag_capacity + 1):
            if i == 0 or w == 0:
                """For this condition, we check if the pellet is zero (which means, we don't have a pellet) and if the 
                capacity of the bag is zero then, the value will also be zero."""
                k[i][w] = 0

            elif list_of_weights[i - 1] <= w:
                """Or if the weight of certain pellet at position i is less than or equal to the weight or capacity of 
                the bag then compute for the maximum value."""
                k[i][w] = max(k[i-1][w], k[i-1][w - list_of_weights[i-1]] + list_of_values[i-1])

            else:
                """Else the value of the pellet at the particular capacity of the bag will be the previous' pellet at 
                that capacity of the bag one on top on it, one at the same """
                k[i][w] = k[i-1][w]

    # Finding which pellets that contributed to the highest value and append the value and its weight
    """Warning: This while loop has takes a lof of time, you may want to comment it to first see the maximum value"""
    while number_of_pellets > 0 and bag_capacity > 0:
        if k[number_of_pellets][bag_capacity] != k[number_of_pellets - 1][bag_capacity]:
            print('\nPellets that contributed to the maximum value are: ')
            print(f"Package {number_of_pellets} with weight {list_of_weights[number_of_pellets - 1]} and value= {list_of_values[number_of_pellets - 1]}")
            bag_capacity = bag_capacity - list_of_weights[number_of_pellets - 1]
            number_of_pellets -= 1

    return f'\nThe highest profit that Burglar can make is: ${k[number_of_pellets][bag_capacity]}'


values = [0, 1200, 1700, 2000, 2500, 3000, 4100, 7000, 7500]
weights = [0, 1, 3, 4, 5, 6, 8, 11, 12]
capacity_of_bag = 20
pellets = 8

print(knapsack(values, weights, capacity_of_bag, pellets))