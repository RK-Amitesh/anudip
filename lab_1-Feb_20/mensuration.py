"""
This program imports module_3D
and calculates CSA, TSA and Volume of:

1. Cylinder
2. Cone
3. Cuboid
"""

# Importing the custom 3D module
import module_3D as m3d


def main():
    """Main function to select shape and perform calculations."""

    print("Choose Shape:")
    print("1. Cylinder")
    print("2. Cone")
    print("3. Cuboid")

    choice = input("Enter your choice (1/2/3): ")

    # ---------------- CYLINDER ----------------
    if choice == "1":
        r = float(input("Enter radius: "))
        h = float(input("Enter height: "))

        print("\nCylinder Results:")
        print("Curved Surface Area:", m3d.cylinder_csa(r, h))
        print("Total Surface Area:", m3d.cylinder_tsa(r, h))
        print("Volume:", m3d.cylinder_volume(r, h))

    # ---------------- CONE ----------------
    elif choice == "2":
        r = float(input("Enter radius: "))
        h = float(input("Enter height: "))

        print("\nCone Results:")
        print("Curved Surface Area:", m3d.cone_csa(r, h))
        print("Total Surface Area:", m3d.cone_tsa(r, h))
        print("Volume:", m3d.cone_volume(r, h))

    # ---------------- CUBOID ----------------
    elif choice == "3":
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        h = float(input("Enter height: "))

        print("\nCuboid Results:")
        print("Curved Surface Area:", m3d.cuboid_csa(l, b, h))
        print("Total Surface Area:", m3d.cuboid_tsa(l, b, h))
        print("Volume:", m3d.cuboid_volume(l, b, h))

    else:
        print("Invalid choice.")


# Ensures the program runs only when executed directly
if __name__ == "__main__":
    main()