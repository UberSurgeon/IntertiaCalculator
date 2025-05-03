

class cylinderTensor:
    def __init__(self, height, radius, mass):
        self.height = height
        self.radius = radius
        self.mass = mass
        self.I11 = 0.0
        self.I22 = 0.0
        self.I33 = 0.0

    def calcTensor(self):
        self.I11 = round((1/12) * self.mass * (3 * (self.radius)**2 + (self.height)**2), 5)
        self.I22 = self.I11
        self.I33 = round((1/2) * self.mass * (self.radius)**2, 5)
        
        return [self.I11, self.I22, self.I33]


def main():
    cy = cylinderTensor(4,1,5)
    print(cy.calcTensor())
    


if __name__ == "__main__":
    main()
