import math
import argparse

parser = argparse.ArgumentParser(description="Calculate area of a rectangule")
parser.add_argument('-c', '--size1', type=int, metavar="", required=True, help="First size")
parser.add_argument('-d', '--size2', type=int, metavar="", required=True, help="Second size")

group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help="print quiet")
group.add_argument('-v', '--verbose', action='store_true', help="print verbose")
arg = parser.parse_args()

def calculateArea(x,y):
	return x*y

if __name__ == '__main__':
	a = 10
	b = 20
	
	print("Area = ",calculateArea(a,b))

	area = calculateArea(arg.size1, arg.size2)
	
	if arg.quiet:
		print("Quiet",area)
	elif arg.verbose:
		print("Verbose",area)
	else:
		print("Conventional, area with parser = ",area)

