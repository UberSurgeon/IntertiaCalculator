class solidEllipsoidtensor:
    def __init__(self, a, b, c, mass):
        self.a = a
        self.b = b
        self.c = c
        self.mass = mass
        self.I11 = 0.0
        self.I22 = 0.0
        self.I33 = 0.0

    def calcTensor(self):
        self.I11 = round((1/5) * self.mass * ((self.b)**2 + (self.c)**2), 5)
        self.I22 = round((1/5) * self.mass * ((self.a)**2 + (self.c)**2), 5)
        self.I33 = round((1/5) * self.mass * ((self.a)**2 + (self.b)**2), 5)

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
