


# # def print_somthing_n_times(something, n_times):
#     """ this function goes from n times to zero, descendgin

#     """
#     while n_times > 0:
#         print(something, n_times)
#         return fib(something, n_times - 1)



# fib('hhhhhell world', 4)




def print_something_ascending(something, n_times, start = 0):
    """ print something n_times in ascending order!

    """
    while start != n_times:
        print(something, start)
        return print_something_ascending(something, n_times, start + 1)
print_something_ascending('hhhhhell world', 4)