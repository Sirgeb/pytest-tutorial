import pytest 
import source.shapes as shapes 
import math 

# -s on the terminal to get the setup and teardown

class TestCircle:
  def setup_method(self, method):
    self.circle = shapes.Circle(10)

  def teardown_method(self, method):
    del self.circle

  def test_area(self):
    assert self.circle.area() == math.pi * self.circle.radius ** 2

  def test_perimeter(self):
    result = self.circle.perimeter()
    expected = 2 * math.pi * self.circle.radius
    assert result == expected 
    
