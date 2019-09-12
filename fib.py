


# def print_somthing_n_times(something, n_times):
#     """ this function goes from n times to zero, descending
#     recursive   
#     """
    
#     while n_times > 0:
#         print(something, n_times)
#         return print_somthing_n_times(something, n_times - 1)
#     return


# print_somthing_n_times('hhhhhell world', 4)
# print(type(print_somthing_n_times('hhhhhell world', 4)))




# def print_something_ascending(something, n_times, start = 0):
#     """ print something n_times in ascending order!
#         recusively, 
#         can set defualt number can be changed,
#         i don't handle if start is greater than n_times, run time error |(or) stack overflow
#     """
#     while start <= n_times: #can put either !=, <, <= depending on whether you want
#     #n_times to be inclusive or exclusive
#         print(something, start)
#         return print_something_ascending(something, n_times, start + 1)

#     return
# print_something_ascending('hhhhhell world', 4)


def factorial(n):
    print('factorial has been called with n = ' + str(n))
    if n == 1:
        return 1
    else:
        result = n * factorial(n - 1)
        print('intermediate result for', n, '* factorial(',n-1, '):', result)
        return result

print(factorial(10))

# print(type(factorial(10)))




