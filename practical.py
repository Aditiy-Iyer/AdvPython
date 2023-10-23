from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius = radius
        print("Radius of the circle:", 6)

    def area(self):
        circle_area = 3.14*radius**2
        print("Area of the circle:", circle_area)

    def perimeter(self):
        circle_perimeter = 2*3.14*radius
        print("Perimeter of the circle:", circle_perimeter)



class square(shape):
    def __init__(self, side):
        self.side = side
        print("Side of the square:", 4)


    def area(self):
        square_area = side**2
        print("Area of the square:", square_area)


    def perimeter(self):
        square_perimeter = side*4
        print("Perimeter of the square:", square_perimeter)

#radius = 4
#circle1 = circle(radius)
#circle_area = circle1.area()
#circle_perimeter = circle1.perimeter()


#side = 4
#square1 = square(side)
#square_area = square1.area()
#square_perimeter = square1.perimeter()

while True:
    print("\nMain Menu")
    print("1. Calculate Area")
    print("2. Calculate Perimeter")
    print("3. Do you want to continue?")
    choice1 = int(input("Enter the Choice:"))

    if choice1 == 1:
        print("\nCalculate Area")
        print("1. Circle")
        print("2. Square")
        choice2 = int(input("Enter the Choice:"))

        if choice2 ==1:
            radius = int(input("Enter Radius of the Circle:"))
            c=circle(radius)
            c.area()

        elif choice2 ==2:
            side = int(input("Enter the side of the square:"))
            s=square(side)
            s.area()

            
    elif choice1 == 2:
        print("\nCalculate Perimeter")
        print("1. Circle")
        print("2. Square")
        choice2 = int(input("Enter the Choice:"))

        if choice2 ==1:
            radius = int(input("Enter Radius of the Circle:"))
            c1 = circle(radius)
            c1.perimeter()
    
        elif choice2 ==2:
            side = int(input("Enter the side of the square:"))
            s1 = square(side)
            s1.perimeter()