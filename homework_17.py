class Rectangular:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def to_sorted_tuple(self):
        return sorted((self.side1, self.side2))

    def __eq__(self, other):
        if not isinstance(other, Rectangular):
            raise TypeError(f"Not supported type {type(other)}")
        return self.to_sorted_tuple() == other.to_sorted_tuple()

    def __gt__(self, other):
        if not isinstance(other, Rectangular):
            raise TypeError(f"Not supported type {type(other)}")
        reg1 = self.to_sorted_tuple()
        reg2 = other.to_sorted_tuple()
        for i in range(2):
            if reg1[i] > reg2[i]:
                return "first object greader than other"
            else:
                return "first object not greader than other"

    def area(self):
        area = self.side1 * self.side2
        return area

    def perimeter(self):
        perimeter = 2 * (self.side1 + self.side2)
        return perimeter

    def is_a_like_rect(self, other):
        reg1 = self.to_sorted_tuple()
        reg2 = other.to_sorted_tuple()
        print(reg1[0]/reg2[0])
        if reg1[0] / reg2[0] == reg1[1] / reg2[1]:
            return True
        else:
            return False


r1 = Rectangular(5, 7)
r2 = Rectangular(3, 4)
r3 = Rectangular(8, 6)

print(r1.__gt__(r2))
print(r1.__eq__(r2))
print(r1.area())
print(r2.perimeter())
print(r2.is_a_like_rect(r3))
print(r2.is_a_like_rect(r1))


