"""Print items in the list, using recursion.

For example::

   >>> print_recursively([1, 2, 3])
   1
   2
   3

"""


def print_recursively(lst):
    """Print items in the list, using recursion."""

    # [1, 2, 3] --> [2,3] --> [3]
    # list slicing involved... lst[1:]

    # BASE CASE
        # when lst empty, stop


    # PROGRESSION
        # print lst[0], then recurse w/ list slicing


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. GREAT JOB!\n"
