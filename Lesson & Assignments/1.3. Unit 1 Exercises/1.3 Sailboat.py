# right half of the sky
Rect(200, 0, 200, 250, fill=gradient('darkSlateBlue', 'slateBlue', start='top'))
# Draw the sail and ocean.
### (HINT: Use the ocean and the left half of the sky to cover part of the
#          sail!)
### Place Your Code Here ###
Oval(200,200,160,240,fill='lightGrey')
Rect(00, 0, 200, 250, fill=gradient('darkSlateBlue', 'slateBlue', start='top'))
Rect(0,250,400,150,fill='steelBlue')
# Draw the hull (base) of the ship.
### (HINT: Use a Polygon, Circle, and a Rectangle.)
### Place Your Code Here ###
Polygon(140,300,120,260,280,260,280,300,fill='midnightBlue')
Circle(280,300,40,fill='midnightBlue')
Rect(140,300,180,40,fill='steelBlue')
# Draw the ropes and mast (the pole holding the sail).
### Place Your Code Here ###
Line(200,80,140,260,lineWidth=2,fill='navy')
Line(200,140,230,260,lineWidth=2,fill='navy')
Line(200,70,200,260,lineWidth=6,fill='midnightBlue')
