import argparse
from complex import Complex
from functools import wraps

def printer(func):
    """
    A decorator for the complex operations to be performed
    """
    @wraps(func) # we do this to make sure the docstring and name of the original function is preserved
    def inner_func(*args, **kwargs): # we can pass both positional argument or keyword argument like this
        output = func(*args, **kwargs) 
        print(f"We performed {func.__name__} and the output was : {output}")
        return output
    return inner_func

@printer
def add_complex(c1, c2):
    return c1 + c2

@printer
def subtract_complex(c1, c2):
    return c1 - c2

@printer
def multiply_complex(c1, c2):
    return c1 * c2

@printer
def divide_complex(c1, c2):
    return c1 / c2

def read_complex_numbers(filename):
    """
    Writes complex number to a txt file.

    Parameters:
    filename : str
        The name / full path of the file to write to.
    complex_numbers : object of complex class
        complex number to write into text file
    """
    complex_numbers = []
    with open(filename, 'r') as file:
        for line in file:
            real, imag = map(lambda x : float(x), line.split(' ')[0:3:2])
            complex_numbers.append(Complex(real, imag))
    return complex_numbers
 

def write_complex_numbers(filename, complex_number):
    """
    Writes complex number to a txt file.

    Parameters:
    filename : str
        The name / full path of the file to write to.
    complex_numbers : object of complex class
        complex number to write into text file
    """
    with open(filename, 'a') as file:
        to_print = "{} + {} i\n".format(complex_number.real,complex_number.imag)
        file.write(to_print)

 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=" Python practice using complex numbers")
    subparsers = parser.add_subparsers(dest="command")

    parser_read = subparsers.add_parser("read", help="Read complex numbers from a file")
    parser_read.add_argument("--filename", type=str, help="The file to read complex numbers from")

    parser_write = subparsers.add_parser("write", help="Write complex number to a file")
    parser_write.add_argument("--filename", type=str, help="The file to write complex number to")
    parser_write.add_argument("--rvalue", type=float, help="Value of real part of a complex number")
    parser_write.add_argument("--ivalue", type=float, help="Value of imaginary part of a complex number")

    parser_operation = subparsers.add_parser("operation", help="Operation to perform on two complex numbers")
    parser_operation.add_argument("--op", choices=["add", "subtract", "multiply", "divide"], help="The operation to perform")
    parser_operation.add_argument("--real1", type=float, help="The real part of the first complex number")
    parser_operation.add_argument("--imag1", type=float, help="The imaginary part of the first complex number")
    parser_operation.add_argument("--real2", type=float, help="The real part of the second complex number")
    parser_operation.add_argument("--imag2", type=float, help="The imaginary part of the second complex number")

    args = parser.parse_args()

    if args.command == "read":
        complex_numbers = read_complex_numbers(args.filename)
        print("Complex numbers read from file:")
        for c in complex_numbers:
            print(c)

    elif args.command == "write":
        complex_numbers = Complex(args.rvalue,args.ivalue)
        write_complex_numbers(args.filename, complex_numbers)
        print("Complex numbers have been written to file.")

    elif args.command == "operation":
        c1 = Complex(args.real1, args.imag1)
        c2 = Complex(args.real2, args.imag2)

        if args.op == "add":
            add_complex(c1, c2)

        elif args.op == "subtract":
            subtract_complex(c1, c2)

        elif args.op == "multiply":
            multiply_complex(c1, c2)

        elif args.op == "divide":
            divide_complex(c1, c2)
 
    
 