import math
import argparse

parser = argparse.ArgumentParser(description="Calculate area of a rectangule")
parser.add_argument('-c', '--size1', type=int, metavar="", help="First size")
parser.add_argument('-d', '--size2', type=int, metavar="", help="Second size")

arg = parser.parse_args()

def calculateArea(x,y):
	return x*y

if __name__ == '__main__':
	a = 10
	b = 20
	
	print("Area = ",calculateArea(a,b))

	print("Area with parser = ",calculateArea(arg.size1, arg.size2))

