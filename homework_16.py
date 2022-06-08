#2
import cmath
import math


class Triangle:

    def __init__(self, side1, side2, side3, height):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.height = height

    def is_valid_triangle(self):
        if self.side1 + self.side2 >= self.side3 and self.side2 + self.side3 >= self.side1 and self.side1 + self.side3 >= self.side2:
            return True
        else:
            return False

    def perimeter(self):
        if self.is_valid_triangle():
            perimeter = self.side1 + self.side2 + self.side3
        else:
            perimeter = "Triangle is not valid"
        return perimeter

    def area(self):
        if self.is_valid_triangle():
            p = (self.side1 + self.side2 + self.side3)/2
            num_ = p * (p - self.side1) * (p -self.side2 ) * (p - self.side3)
            area = math.sqrt(num_)
            print(num_)
        else:
            area = "Triangle is not valid"
        return area

    def compare_triangles(self, other):
        if self.is_valid_triangle() and other.is_valid_triangle():
            if self.side1 / other.side1 == self.side2 / other.side2 == self.side3 / other.side3:
                print("triangles is compare ")
            else:
                print("triangles is not compare")
        else:
            print("Triangle is not valid")


t1 = Triangle(3, 4, 5, 6)
t2 = Triangle(6, 8, 10, 12)
t3 = Triangle(4, 5, 78, 43)


print(t1.is_valid_triangle())
print(t1.perimeter())
print(t1.area())
print(t1.compare_triangles(t2))
print(t3.perimeter())
print(t3.area())
print(t3.compare_triangles(t2))





#1


import random

rand = [random.randint(0, 9) for n in range(4)]
print(rand)


class Guess:
    def __init__(self, num1, num2, num3, num4):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4

    def game(self):
        cow = 0
        bull = 0
        finish_cows = 0
        finish_bulls = 0
        guess_num = [self.num1, self.num2, self.num3, self.num4]
        print(guess_num)
        if guess_num == rand:
            print("Congratulations, you guessed it")
        else:

            for i in range(4):
                if guess_num[i] == rand[i]:
                    cow += 1
                if guess_num[i] in rand:
                    bull += 1

            print(f"you have {cow} cows and {bull} bulls")
