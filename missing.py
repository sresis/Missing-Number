"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8
    
    """
    # turn list into set
    nums_set = set(nums)
    min_num = 1
    #go through list and check if number before and after it is there
    # but if it is min or max, change the logic
    for item in nums_set:
        if item == min_num:  
            if (item + 1) not in nums_set:
                return (item + 1)
        elif item == max_num:
            if (item - 1) not in nums_set:
                return (item - 1)
        elif (item + 1) not in nums_set:
            return (item + 1)
        elif (item - 1) not in nums_set:
            return (item - 1)
        



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. NICELY DONE!\n")
