__author__ = 'aldo_martini'


class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

        if self.numerator < 0 and self.denominator < 0:
            self.numerator = abs(self.numerator)
            self.denominator = abs(self.denominator)

    def __repr__(self):
        if self.numerator == self.denominator:
            return '1'
        elif self.numerator == abs(self.denominator):
            return '-1'
        else:
            for i in range(0,self.numerator-1):
                simplificator = self.numerator - i
                if self.numerator == self.denominator:
                    return 1
                if self.numerator == -(self.denominator) or -(self.numerator) == self.denominator:
                    return -1
                if self.numerator % simplificator == 0 and self.denominator % simplificator == 0:
                    self.numerator = self.numerator / simplificator
                    self.denominator = self.denominator / simplificator
                if abs(self.numerator) == 1:
                    break
            if self.denominator == 1:
                return("{}".format(int(self.numerator)))
            else:
                return("{}/{}".format(int(self.numerator), int(self.denominator)))

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Rational(new_numerator, new_denominator)

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __lt__(self, other):
        if self.numerator/self.denominator > 0 and other.numerator/other.denominator > 0:
            return self.numerator * other.denominator < other.numerator * self.denominator
        elif self.numerator/self.denominator < 0 and other.numerator/other.denominator < 0:
            return not(self.numerator * other.denominator < other.numerator * self.denominator)
        elif self.numerator/self.denominator > 0 and other.numerator/other.denominator < 0:
            return False
        else:
            return True

    def __eq__(self, other):
        if self.numerator/self.denominator > 0 and other.numerator/other.denominator > 0:
            return self.numerator * other.denominator == other.numerator * self.denominator
        elif self.numerator/self.denominator < 0 and other.numerator/other.denominator < 0:
            return self.numerator * other.denominator == other.numerator * self.denominator
        else:
            return False




r = Rational(-4,-4)
r1 = Rational(-1,-1)
print(r1)
print(r<r1)
