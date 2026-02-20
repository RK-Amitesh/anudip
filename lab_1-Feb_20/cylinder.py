"""
Program to calculate:
- Curved Surface Area (CSA)
- Total Surface Area (TSA)
- Volume

Of a Cylinder using module_3D.
"""

# Importing the custom 3D module
import module_3D as m3d


# Taking user input
radius = float(input("Enter radius of cylinder: "))
height = float(input("Enter height of cylinder: "))

# Calling module functions
csa = m3d.cylinder_csa(radius, height)
tsa = m3d.cylinder_tsa(radius, height)
volume = m3d.cylinder_volume(radius, height)

# Displaying results
print("\nCylinder Results")
print("Curved Surface Area:", csa)
print("Total Surface Area:", tsa)
print("Volume:", volume)