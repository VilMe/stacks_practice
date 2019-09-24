
numb_list = [30, 50, 3, 53, 4, 2, 10, 12]


def find_min(list_of_numbs):
    """find local minimum and return value and index, figure out how to 
    import doctest, run doc testing...

    """
    lowest_val = list_of_numbs[0]
    index_of_l_v = 0

    for place in range(len(list_of_numbs)):
        #print(place, list_of_numbs[place])
        if list_of_numbs[place] < lowest_val:
            lowest_val = list_of_numbs[place]
            index_of_l_v = place
    return f"minimum of list is {lowest_val} at index of {index_of_l_v}"


what_is_min = find_min(numb_list)

print(what_is_min)