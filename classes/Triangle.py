class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

# Add your Triangle class below!
class Triangle(Shape):
  def __init__(self, side1, side2, side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3

  def check_angles(self):
    sum = self.side1 + self.side2 + self.side3
    if sum == 180:
      return True
    else:
      return False


my_triangle = Triangle(30,60,90)

print my_triangle.number_of_sides
print my_triangle.check_angles()

class Equilateral(Triangle):
  angle = 60
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle