app.background = gradient('black', 'midnightBlue', start='top')
# Draw the alien body.
### (Hint: Use 7 shapes.)
### Place Your Code Here ###
Circle(200,200,100,fill='limeGreen')
Circle(100,200,20,fill='limeGreen')
Circle(150,290,20,fill='limeGreen')
Circle(250,290,20,fill='limeGreen')
Circle(300,200,20,fill='limeGreen')
Circle(200,245,25)
Rect(175,220,50,25,fill='limeGreen')
# Write a function that draws one eye.
def drawEye(x, y, e, p):
    ### Place Your Code Here ###
    Circle(x,y,e,fill='white')
    Circle(x,y,p)

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawEye(200, 175, 55, 27)
