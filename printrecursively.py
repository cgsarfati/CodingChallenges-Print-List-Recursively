"""Print items in the list, using recursion.

For example::

   >>> print_recursively([1, 2, 3])
   1
   2
   3

"""


def print_recursively(lst):
    """Print items in the list, using recursion."""

    # e.g. [1, 2, 3] --> [2,3] --> [3]
    # list slicing involved... lst[1:]

    # BASE CASE
        # when lst empty, stop
    # PROGRESSION
        # print lst[0], then recurse w/ list slicing

    # while lst not empty
    if lst:
        # print 1st item
        print lst[0]
        # slice, recurse
        print_recursively(lst[1:])


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. GREAT JOB!\n"
