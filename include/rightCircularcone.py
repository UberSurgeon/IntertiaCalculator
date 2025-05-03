class rightCircularconetensor:
    def __init__(self, height, radius, mass):
        self.height = height
        self.radius = radius
        self.mass = mass
        self.I11 = 0.0
        self.I22 = 0.0
        self.I33 = 0.0

    def calcTensor(self):
        self.I11 = round(((3/5) * self.mass * (self.height)**2) + ((3/20) * self.mass * (self.radius)**2), 5)
        self.I22 = self.I11
        self.I33 = round((3/10) * self.mass * (self.radius)**2, 5)

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
