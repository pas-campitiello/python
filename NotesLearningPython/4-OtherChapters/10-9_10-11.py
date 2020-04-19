# Common data archiving and compression formats are directly supported 
# by modules including: zlib, gzip, bz2, lzma, zipfile and tarfile.
import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))
print(zlib.crc32(s))


print()
# Python provides a measurement tool that answers those questions immediately.
# For example, it may be tempting to use the tuple packing and unpacking feature 
# instead of the traditional approach to swapping arguments. 
# The timeit module quickly demonstrates a modest performance advantage:
from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())


print()
# The doctest module provides a tool for scanning a module 
# and validating tests embedded in a program’s docstrings. 
# Test construction is as simple as cutting-and-pasting a typical call along with its results into the docstring. 

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests, it prints nothing if test passes

print()
# The unittest module is not as effortless as the doctest module, 
# but it allows a more comprehensive set of tests to be maintained in a separate file:

import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests
