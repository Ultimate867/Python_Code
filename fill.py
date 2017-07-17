# Junior Peralta
# April 9, 2014
# fill.py
# Fill in the missing function definitions
# Write the functions setUp(), userInput(), displayLine() and conclusion().
# Include all functions, including the main() above in the file you submit. 

from graphics import*

def setUp():
    win = GraphWin("Line",500,500)
    return win

def userInput():
    x1 = eval(input("Enter first x-coordinate: "))
    y1 = eval(input("Enter first y-coordinate: "))
    x2 = eval(input("Enter second x-coordinate: "))
    y2 = eval(input("Enter second y-coordinate: "))
    return x1, y1, x2, y2

def displayLine(w,x1,y1,x2,y2):
     line = Line(Point(x1,y1), Point(x2, y2))
     line.draw(w)

def conclusion(w):
    w.getMouse()
    w.close()

def main():
    w = setUp()	#Creates and returns a graphics window
    x1,y1,x2,y2 = userInput()#Asks user for 4 inputs and returns numbers entered
    displayLine(w,x1,y1,x2,y2)#Draws a line from (x1,y1) to (x2,y2) on window w
    conclusion(w)#Gets a mouse click and closes window w

main()

    



















main()
