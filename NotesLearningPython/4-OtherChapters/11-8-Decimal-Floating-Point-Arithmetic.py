# The decimal module offers a Decimal datatype for decimal floating point arithmetic.
from decimal import *

print(round(Decimal('0.70') * Decimal('1.05'), 2))
print(round(.70 * 1.05, 2))

# The Decimal result keeps a trailing zero, 
# automatically inferring four place significance from multiplicands with two place significance. 
# Decimal reproduces mathematics as done by hand and avoids issues that can arise 
# when binary floating point cannot exactly represent decimal quantities.

# Exact representation enables the Decimal class to perform modulo calculations 
# and equality tests that are unsuitable for binary floating point
print()
print(Decimal('1.00') % Decimal('.10'))
print(1.00 % 0.10)

print()
print(sum([Decimal('0.1')]*10), " = Decimal('1.0') ?", sum([Decimal('0.1')]*10) == Decimal('1.0'))
print(sum([0.1]*10), " = 1.0 ?", sum([0.1]*10)  == 1.0)

#The decimal module provides arithmetic with as much precision as needed:
print()
getcontext().prec = 36
print(Decimal(1) / Decimal(7))

