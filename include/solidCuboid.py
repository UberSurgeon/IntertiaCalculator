class solidCuboidtensor:
    def __init__(self, height, width, depth, mass):
        self.height = height
        self.width = width
        self.depth = depth
        self.mass = mass
        self.I11 = 0.0
        self.I22 = 0.0
        self.I33 = 0.0

    def calcTensor(self):
        self.I11 = round((1/12) * self.mass * ((self.height)**2 + (self.depth)**2), 5)
        self.I22 = round((1/12) * self.mass * ((self.width)**2 + (self.height)**2), 5)
        self.I33 = round((1/12) * self.mass * ((self.width)**2 + (self.depth)**2), 5)

        return [self.I11, self.I22, self.I33]

    def calcMatrix(self):
        return f"""
[
    [{self.I11}, 0, 0]
    [0, {self.I22}, 0]
    [0, 0, {self.I33}]
]
        """

    def calcURDF(self):
        return f"""
<inertia ixx="{self.I11}" ixy="0" ixz="0" iyy="{self.I22}" iyz="0" izz="{self.I33}" />
    """


def main():
    pass


if __name__ == "__main__":
    main()
