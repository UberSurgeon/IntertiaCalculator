from include import solidCylinder, solidSphere, hollowSphere, rightCircularcone, solidCuboid, solidEllipsoid, thickWallcylinopenend
import sys


def cSolidsphere():
    radius = float(input("radius: "))
    mass = float(input("mass: "))
    ss = solidSphere.solidSpheretensor(radius, mass)
    print(ss.calcTensor())
    print(ss.calcMatrix())
    print(ss.calcURDF())


def cHollowsphere():
    radius = float(input("radius: "))
    mass = float(input("mass: "))
    hs = hollowSphere.hollowSpheretensor(radius, mass)
    print(hs.calcTensor())
    print(hs.calcMatrix())
    print(hs.calcURDF())


def cSolidellipsoid():
    a = float(input("semi-axes a: "))
    b = float(input("semi-axes b: "))
    c = float(input("semi-axes c: "))
    mass = float(input("mass: "))
    se = solidEllipsoid.solidEllipsoidtensor(a, b, c, mass)
    print(se.calcTensor())
    print(se.calcMatrix())
    print(se.calcURDF())


def cRightcircularcone():
    radius = float(input("radius: "))
    height = float(input("height: "))
    mass = float(input("mass: "))
    rc = rightCircularcone.rightCircularconetensor(height, radius, mass)
    print(rc.calcTensor())
    print(rc.calcMatrix())
    print(rc.calcURDF())


def cSolidcuboid():
    width = float(input("width: "))
    height = float(input("height: "))
    depth = float(input("depth: "))
    mass = float(input("mass: "))
    scu = solidCuboid.solidCuboidtensor(height, width, depth, mass)
    print(scu.calcTensor())
    print(scu.calcMatrix())
    print(scu.calcURDF())


def cSolidcylinder():
    radius = float(input("radius: "))
    height = float(input("height: "))
    mass = float(input("mass: "))
    sc = solidCylinder.solidCylindertensor(height, radius, mass)
    print(sc.calcTensor())
    print(sc.calcMatrix())
    print(sc.calcURDF())


def cThickwalledcylinopenend():
    r1 = float(input("inner-radius: "))
    r2 = float(input("outter-radius: "))
    height = float(input("height: "))
    mass = float(input("mass: "))
    tc = thickWallcylinopenend.thickWallcylinopenend(height, mass, r1 ,r2)
    print(tc.calcTensor())


def inputManager():
    choice = int(input("Select a number 0-7: "))
    if choice == 1:
        cSolidsphere()
    elif choice == 2:
        cHollowsphere()
    elif choice == 3:
        cSolidellipsoid()
    elif choice == 4:
        cRightcircularcone()
    elif choice == 5:
        cSolidcuboid()
    elif choice == 6:
        cSolidcylinder()
    elif choice == 7:
        cThickwalledcylinopenend()
    else:
        sys.exit(0)

    if str(input("Countinue?(y/n): ")).lower() != "y":
        sys.exit(0)
    print("\n")

def guiMenu():
    while True:
        print("Calculator for 3D inertia tensors")
        print("*********************************")
        print("""
    1. Solid Sphere
    2. Hollow Sphere
    3. Solid Ellipsoid
    4. Right Circular Cone
    5. Solid Cuboid
    6. Solid Cylinder
    7. Thick-Walled Cylindrical Tube, Open Ends
    0. Exit
            """)
        print("*********************************")
        inputManager()


def main():
    pass


if __name__ == "__main__":
    main()
