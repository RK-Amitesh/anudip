"""
import_demo.py

This file demonstrates different ways to import
functions from the numeric_calculation module.
"""

# -------------------------------------------------
# METHOD 1: Import the entire module
# -------------------------------------------------
# We must use module_name.function_name()

import numeric_calculation

print("METHOD 1: Import entire module")
numeric_calculation.displaysum(10, 5)
print("Returned Product:", numeric_calculation.calculateproduct(10, 5))

print("\n-----------------------------------\n")


# -------------------------------------------------
# METHOD 2: Import module with alias
# -------------------------------------------------
# We use a shorter name for convenience

import numeric_calculation as nc

print("METHOD 2: Import with alias")
nc.displaydifference(20, 7)
print("Returned Sum:", nc.calculatesum(8, 2))

print("\n-----------------------------------\n")


# -------------------------------------------------
# METHOD 3: Import specific functions
# -------------------------------------------------
# Now we can directly call the function
# without using module name

from numeric_calculation import calculatequotient, displayproduct

print("METHOD 3: Import specific functions")
displayproduct(6, 3)

try:
    print("Returned Division:", calculatequotient(10, 2))
except ZeroDivisionError as error:
    print("Error:", error)

print("\n-----------------------------------\n")


# -------------------------------------------------
# METHOD 4: Import everything
# -------------------------------------------------
# This imports all functions directly into
# current namespace. Can cause name conflicts.

from numeric_calculation import *

print("METHOD 4: Import * ")
displaysum(3, 3)
print("Returned Difference:", calculatedifference(9, 4))

print("\n-----------------------------------\n")


print("All import methods demonstrated successfully.")