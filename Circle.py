from math import pi


class Circle:

    def __init__(self, radius):
        # print("Object created.")
        """
        Loo klass koos raadiusega.
        """
        self.radius = radius

    def get_radius(self):
        # print("Return radius.")
        # Tegelikult seda vaja pole
        return self.radius

    def get_diameter(self):
        return 2 * self.radius

    def get_area(self):
        # pi * pow(self.radius, 2) # import pow
        return pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * pi * self.radius

    def show_circle_data(self):
        print('Radius:', self.radius)
        print('Diameter:', self.get_diameter())
        print('Area:', self.get_area())
        print('Perimeter:', self.get_perimeter())
