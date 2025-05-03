class thickWallcylinopenend:
    def __init__(self, height, mass, innerRadius, outerRadius):
        self.height = height
        self.innerRadius = innerRadius
        self.outerRadius = outerRadius
        self.mass = mass
        self.I11 = 0.0
        self.I22 = 0.0
        self.I33 = 0.0

    def calcTensor(self):
        m = self.mass
        r2sqr = self.outerRadius**2
        r1sqr = self.innerRadius**2
        hsqr = self.height**2
        self.I11 = round((1/12) * m * (3 * (r2sqr + r1sqr) + hsqr) , 5)
        self.I22 = self.I11
        self.I33 = round((1/2) * m * (r2sqr + r1sqr), 5)

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
