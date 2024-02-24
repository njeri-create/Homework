class Rectangle():
     def __init__(self,length,width):
         self.length = length
         self.width = width

     def area(self):
         print(self.area)
     def multiplication_rectangle(self):
          self.area = self.length * self.width


rectangle1 = Rectangle(48,50)
rectangle2 = Rectangle(56,45)
rectangle3 = Rectangle(40,45)
print(rectangle1.length,rectangle2.length,rectangle3.length)
print(rectangle1.width,rectangle2.width,rectangle3.width)
rectangle1.multiplication_rectangle()
print(rectangle1.area)
rectangle2.multiplication_rectangle()
print(rectangle2.area)
rectangle3.multiplication_rectangle()
print(rectangle3.area)

