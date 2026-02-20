"""
Reusable module to calculate:
- Curved Surface Area (CSA)
- Total Surface Area (TSA)
- Volume

For:
1. Cylinder
2. Cone
3. Cuboid
"""

import math


# -------------------- CYLINDER --------------------

def cylinder_csa(radius, height):
    """Return Curved Surface Area of Cylinder."""
    return 2 * math.pi * radius * height


def cylinder_tsa(radius, height):
    """Return Total Surface Area of Cylinder."""
    return 2 * math.pi * radius * (radius + height)


def cylinder_volume(radius, height):
    """Return Volume of Cylinder."""
    return math.pi * radius**2 * height


# -------------------- CONE --------------------

def cone_csa(radius, height):
    """Return Curved Surface Area of Cone."""
    slant_height = math.sqrt(radius**2 + height**2)
    return math.pi * radius * slant_height


def cone_tsa(radius, height):
    """Return Total Surface Area of Cone."""
    slant_height = math.sqrt(radius**2 + height**2)
    return math.pi * radius * (radius + slant_height)


def cone_volume(radius, height):
    """Return Volume of Cone."""
    return (1/3) * math.pi * radius**2 * height


# -------------------- CUBOID --------------------

def cuboid_tsa(length, breadth, height):
    """Return Total Surface Area of Cuboid."""
    return 2 * (length*breadth + breadth*height + height*length)


def cuboid_volume(length, breadth, height):
    """Return Volume of Cuboid."""
    return length * breadth * height


def cuboid_csa(length, breadth, height):
    """Return Lateral/Curved Surface Area of Cuboid."""
    return 2 * height * (length + breadth)