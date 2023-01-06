# This draws the background; the two lines overlap and create a checkerboard
# pattern!
Line(200, 0, 200, 400, fill='lightGrey', lineWidth=400, dashes=True)
Line(0, 200, 400, 200, fill='cornflowerBlue', lineWidth=400, dashes=True,
     opacity=50)
# plunger
Circle(305, 50, 8, fill=gradient('sienna', 'saddleBrown', start='left'))
Rect(297, 50, 16, 290, fill=gradient('sienna', 'saddleBrown', start='left'))
Rect(290, 340, 30, 15, fill=gradient('red', 'maroon', start='left'))
Circle(305, 410, 60, fill=gradient('red', 'maroon', start='left'))
Rect(245, 390, 120, 10, fill=gradient('crimson', 'darkRed', start='left'))
# paper roll
Rect(85, 75, 100, 50, fill='white')
Oval(85, 100, 20, 50, fill='white')
Oval(185, 100, 20, 50, fill='gainsboro')
# holder
Polygon(185, 90, 185, 110, 210, 90, 210, 70, fill='silver')
Polygon(100, 70, 100, 75, 90, 75, fill='silver')
l=Line(125,100,125,100,lineWidth=100,fill='white')
# Define the paper variable.
### (HINT: The toilet paper is a line with a large lineWidth.)
### Fix Your Code Here ###
# paper =
def onMousePress(x, y):
    # Draw a new perforation line across the toilet paper.
    ### (HINT: Use either y1 or y2 of the paper variable to help get the
    #          y values!)
    ### Place Your Code Here ###
    # Make the paper longer.
    ### Place Your Code Here ###
    l.y2 += 50
    Line(75, l.y2-25, 175,l.y2-25,dashes=True,lineWidth=1)
