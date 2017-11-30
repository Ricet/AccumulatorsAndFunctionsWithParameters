"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Tiarnan Rice.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math

def main():
    """ Calls the   TEST   functions in this module. """
    # run_test_sum_cosines()
    run_test_sum_square_roots()


def run_test_sum_cosines():
    """ Tests the   sum_cosines   function. """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function.
    #   It TESTS the  sum_cosines  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_cosines   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = -0.2358
    answer = sum_cosines(5)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    # Test 2:
    expected = -0.4174
    answer = sum_cosines(10)
    print('Test 2 expected:', expected)
    print('       actual:  ', answer)

    # Test 3:
    expected = 1.229
    answer = sum_cosines(27)
    print('Test 3 expected:', expected)
    print('       actual:  ', answer)

def sum_cosines(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the cosines of the integers
       0, 1, 2, 3, ... n, inclusive, for the given n.
    Side effects:   None.
    Example:
      If n is 3, this function returns
        cos(0) + cos(1) + cos(2) + cos(3)   which is about 0.13416.
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_cosines  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------
    sum = 0;
    for i in range(n + 1):
        sum = sum + math.cos(i)

    return sum


def run_test_sum_square_roots():
    """ Tests the   sum_square_roots   function. """
    # ------------------------------------------------------------------
    # DONE: 4. Implement this function.
    #   It TESTS the  sum_square_roots  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_square_roots   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 11.8544
    answer = sum_square_roots(5)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    # Test 2:
    expected = 57.23208667
    answer = sum_square_roots(15)
    print('Test 2 expected:', expected)
    print('       actual:  ', answer)

    # Test 3:
    expected = 135.6640253
    answer = sum_square_roots(27)
    print('Test 3 expected:', expected)
    print('       actual:  ', answer)

def sum_square_roots(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the square roots of the integers
       2, 4, 6, 8, ... 2n    inclusive, for the given n.
           So if n is 7, the last term of the sum is
           the square root of 14 (not 7).
    Side effects:   None.
    Example:
      If n is 5, this function returns
         sqrt(2) + sqrt(4) + sqrt(6) + sqrt(8) + sqrt(10),
      which is about 11.854408.
    """
    # ------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_square_roots  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------
    sum = 0
    for i in range(n + 1):
        sum = sum + math.sqrt(2 * i)

    return sum

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
