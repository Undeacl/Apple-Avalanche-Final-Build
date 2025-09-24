#Apple Class

import turtle as trtl
wn = trtl.Screen()

class Apple():

  #create different turtles with unique coordinate
  def __init__(self, x, y, apple_id):
    print("apple " + apple_id)
    self.image = "apple.gif"
    self.apple_id = apple_id
    self.letter = trtl.Turtle()
    self.apple = trtl.Turtle()
    self.apple_x = x
    self.apple_y = y
    self.letter.teleport((x-19), (y-35))
    self.apple.teleport(x,y)


  #draw the turtle in
  def draw_apple_and_letter(self):
    wn.addshape(self.image) # Make the screen aware of the new file
    self.apple.shape(self.image)
    self.letter.color("white")
    self.letter.write(self.apple_id, font=("Arial", 35, "bold"))
    wn.update()

  #make the specific turtle fall
  def fall(self):
    y = self.apple.ycor()
    x = self.apple.xcor()
    self.apple.penup()
    self.letter.hideturtle()
    self.letter.clear()
    while y > -150:
      self.apple.goto(x, y)
      y -= 5
    self.apple.pendown()

  def reset_all(self):
    self.apple.clear()
    self.apple.hideturtle()
    self.apple.penup()
    self.letter.clear()
    self.letter.hideturtle()
    self.letter.penup()