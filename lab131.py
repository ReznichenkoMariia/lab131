import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def name(self):
        return "Triangle"

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    def name(self):
        return "Rectangle"


class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        return ((self.a + self.b) / 2) * math.sqrt(self.c ** 2 - ((self.a - self.b) ** 2 / 4))

    def name(self):
        return "Trapeze"


class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.h

    def name(self):
        return "Parallelogram"


class Circle:
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * self.r ** 2

    def name(self):
        return "Circle"


def read_figures(filename):
    figures = []

    try:
        file = open(filename, 'r', encoding='utf-8')

        for line in file:
            line = line.strip()
            if line == "":
                continue

            parts = line.split()
            name = parts[0]
            params = []
            for i in range(1, len(parts)):
                params.append(float(parts[i]))

            if name == "Triangle" and len(params) == 3:
                fig = Triangle(params[0], params[1], params[2])
                figures.append(fig)

            elif name == "Rectangle" and len(params) == 2:
                fig = Rectangle(params[0], params[1])
                figures.append(fig)

            elif name == "Trapeze" and len(params) == 4:
                fig = Trapeze(params[0], params[1], params[2], params[3])
                figures.append(fig)

            elif name == "Parallelogram" and len(params) == 3:
                fig = Parallelogram(params[0], params[1], params[2])
                figures.append(fig)

            elif name == "Circle" and len(params) == 1:
                fig = Circle(params[0])
                figures.append(fig)

            else:
                print("Не вдалося прочитати рядок:", line)

        file.close()

    except FileNotFoundError:
        print("Файл", filename, "не знайдено")

    return figures


def main():
    filename = "input01.txt"
    figures = read_figures(filename)


    for i in range(len(figures)):
        fig = figures[i]
        print(f"{i + 1}. {fig.name()}:")
        print(f"   Периметр: {fig.perimeter():.2f}")
        print(f"   Площа: {fig.area():.2f}")
        print()

    max_area = -1
    max_area_figure = None

    for fig in figures:
        if fig.area() > max_area:
            max_area = fig.area()
            max_area_figure = fig

    max_perimeter = -1
    max_perimeter_figure = None

    for fig in figures:
        if fig.perimeter() > max_perimeter:
            max_perimeter = fig.perimeter()
            max_perimeter_figure = fig


    print("Фігура з найбільшою площею:")
    print(f"   Тип: {max_area_figure.name()}")
    print(f"   Площа: {max_area_figure.area():.2f}")
    print(f"   Периметр: {max_area_figure.perimeter():.2f}")
    print()

    print("Фігура з найбільшим периметром:")
    print(f"   Тип: {max_perimeter_figure.name()}")
    print(f"   Периметр: {max_perimeter_figure.perimeter():.2f}")
    print(f"   Площа: {max_perimeter_figure.area():.2f}")

main()