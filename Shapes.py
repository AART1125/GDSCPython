#This is a simple program about shapes to learn more about an essential topic in OOP: 
# Encapsulation, Inheritance, and Polymorphism
class Shape():
    #private classes are denoted by the __<attribute name> format
    def __init__(self, height, width) -> None:
        self.__width = width
        self.__height = height
    
    def __str__(self) -> str:
        return "Im just a random shape"
    
    #There are two ways to encapsulate an attribute:
    #@property decorator
    #standard getter setter
    
    #@property encapsulation
    #this will make sure that the attribute will not be accessed directly
    #instead the program will make you call the property name and depending on what you do
    #it will either call or set the value of the attribute
    
    @property #Accessing of the Attribute AKA Getter
    def height(self):
        return self.__height
    
    @property
    def width(self):
        return self.__width
    
    @height.setter #Setting of the value of an attribute AKA Setter
    def height(self, height):
        self.__height = height
    
    @width.setter    
    def width(self, width):
        self.__width = width
    
    #Standard Getter and Setter
    #This is the standard format of setting and getting in a class in multiple OOP languages
    #This involves you creating a setter or getter function that you will call in the program
    #Unlike the previous one, the setter here takes in a parameter instead of just assigning an equal sign
    def getheight(self):
        return self.__height
    
    def getwidth(self):
        return self.__width
    
    def setheight(self, height):
        self.__height = height
    
    def setwidth(self, width):
        self.__width = width
    
    def getArea(self):
        return self.__height * self.__width
    
#child inheriting the shape class
class Rectangle(Shape):
    def __init__(self, height, width) -> None:
        #Uses the initializer of the super class
        super().__init__(height, width)
        
    def __str__(self) -> str:
        return "Rectangle"

#child inheriting the shape class
class Square(Shape):
    def __init__(self, height, width) -> None:
        if height == width:
            super().__init__(height,width)
        else:
            print("This is not a square")
            return None
        
    def __str__(self) -> str:
        return "Square"
    
    @property
    def height(self):
        return super().height

    @property
    def width(self):
        return super().width
    
    @height.setter
    def height(self, height):
        if height == self.width:
            super().height = height
        else:
            print("This isn't a square")
            
    @width.setter
    def width(self, width):
        if width == self.height:
            super().width = width
        else:
            print("This isn't a square")
            
    #Example of a polymorphism attribute in OOP since this method has the same method name as the parent class
    #Except it has a different computation from the parent class
    def getArea(self):
        return self.height**2
            
poly1 = Rectangle(2.5,3.5)
poly2 = Square(1.5, 1.5)

#which one will work? Line 51 or Line 52
#print(poly1, poly1.getArea(), poly1.__height, poly1.__width, sep="\n")
print(poly1, poly1.getArea(), poly1.height, poly1.width, sep="\n")

#Which code will work? Line 88 to 89, Line 91 to 92, or Line 94 to 95
print(poly2, poly2.getArea(), poly2.height, poly2.width, sep="\n")
poly2.__height = 2
poly2.__width = 2

poly2.height = 2
poly2.width = 2

print(poly2, poly2.getArea(), poly2.height, poly2.width, sep="\n")