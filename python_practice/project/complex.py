import math


class Numbers():
    """
    A parent class for complex number to practice inheritence
    """
    def __init__(self,real,imag) :
        self.real = real
        self.imag = imag


class Complex(Numbers):
    """
    A class to represent a complex number.
    """
    # constructor
    def __init__(self, real, imag):
        """
        Constructor for the complex class

        Parameters:
        real : float  
        imag : float 
        """
        super().__init__(real,imag)


    # dunder method practice
    def __repr__(self):
        """
        Returns string in proper complex format to print.
    
        Returns:
            The string representation of the complex number.
        """
        return "{} + {} i".format(self.real,self.imag)

    # operator overloading
    def __add__(self, another):
        """
        Operator overloading of the + operator

        Parameters:
        other : Complex ( Complex Number to be added)

        Returns:
        Complex
            The sum of two complex number
        """
        return Complex(self.real + another.real, self.imag + another.imag)

    def __sub__(self, another):
        """
        Operator overloading of the - operator

        Parameters:
        other : Complex ( Complex Number to be subtracted)

        Returns:
        Complex
            The difference of two complex number
        """
        return Complex(self.real - another.real, self.imag - another.imag)

    def __mul__(self, other):
        """
        Operator overloading of the * operator

        Parameters:
        other : Complex ( Complex Number to be multiplied)

        Returns:
        Complex
            The multiplication of two complex number
        """
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        """
        Operator overloading of the / operator

        Parameters:
        other : Complex ( Complex Number to be divided)

        Returns:
        Complex
            The division of two complex number
        """
        try:
            denominator = other.real**2 + other.imag**2 # doing rationalization
            real = (self.real * other.real + self.imag * other.imag) / denominator
            imag = (self.imag * other.real - self.real * other.imag) / denominator
            return Complex(real, imag)
        except ZeroDivisionError:
            raise ValueError("Division by zero error occured")
            


    def magnitude(self):
        """
        Calculates the magnitude of the complex number.

        Returns:
        float
            The magnitude of the complex number.
        """
        return math.sqrt(self.real**2 + self.imag**2)


