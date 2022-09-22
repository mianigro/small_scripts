# Binary Search Theory
# Takes the middle index and checks if the index is the right number or to high or low
# The algorithm then determines if the search value is bigger or small than the middle value
# The algorihm then finds the middle between the middle and the high/low depending
# This is repeated until the end of the list or the value is found

# Binary search function
def binary_search(data_list, goal):

    # Sorts the input list from smallest to biggest value which is required for a binary search
    data_list.sort()

    # Setting boolean function for if the value is found
    reached_goal = False

    # This sets the low index and the high index of the list
    low = 0
    high = len(data_list) - 1

    # Itteration counter
    n = 0

    # Sorting function - checks if the high and low values are the same or the reached_goal is true
    while low <= high and reached_goal == False:
        # Loop itteration counter
        n += 1

        # This function finds the middle index between the high and low without decimals us the floor function to round down
        middle = (low + high) // 2

        # Checks if the middle value is the goal value
        if data_list[middle] == goal:
            print("It is at data index %i, found in %i itterations" % (middle, n))
            reached_goal = True

        # If middle is greater than searched number, it searches up
        elif data_list[middle] > goal:
            high = middle - 1

        # If middle is less than searched number, it searches down
        elif data_list[middle] < goal:
            low = middle + 1

    # This is the break point if the value isn't found
    if low >= high and reached_goal == False:
        print("Data not found in list and did %i searches" % n)

    return middle, n


# Search data
list_searching = [27, 5, 1, 25, 10, 6, 22, 3, 11, -1, 2, 7, -3, 4, 9]
search_goal = 11

# Function to run
binary_search(list_searching, search_goal)
