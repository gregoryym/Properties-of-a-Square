###This program was written for my Ap physics 1 class, test 1
from math import sqrt

print("this program calculates either the area or the perimeter of a square") 
diagonal = input("Input the measurement of the diagonal: ")
choice = input("Do you want the area or the perimeter of a square?: ")


if choice.lower() == "area":
 	 answer = (sqrt(2) * float(diagonal) / float(2)) **2
  	print "The area of the square with diagonal length measuring " + str(diagonal) + " meters      is " + str(answer) + " meters squared"
elif choice.lower() == "perimeter":
   answer = 4 * (float(diagonal) * sqrt(2))
 	 print "The perimeter of the square with diagonal length measuring " + str(diagonal) + " meters is " + str(answer) + " meters"
