TOLERANCE = 10**-10

class MyComplex:
    def __init__(self, r = None, i = None):
        assert (i == None) == (r == None), "Two or zero arguments expected; one given"
        r = 0 if r == None else r
        i = 0 if i == None else i
        self.real = r
        self.imaginary = i

    def conj(self):
        return MyComplex(self.real, -self.imaginary)

    def inverse(self):
        return ~self / self.magsquared()

    def magnitude(self):
        return self.magsquared() ** 0.5

    def magsquared(self):
        return self.real*self.real + self.imaginary*self.imaginary

    def __repr__(self):
        sign = "-" if self.imaginary < 0 else "+"
        return f"{self.real} {sign} {abs(self.imaginary)}i"

    def __add__(self, other):
        if (isinstance(other, MyComplex)):
            return MyComplex(self.real + other.real, self.imaginary + other.imaginary)
        else:
            return MyComplex(self.real + other, self.imaginary)

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if (isinstance(other, MyComplex)):
            return MyComplex(
                self.real * other.real - self.imaginary * other.imaginary,
                self.real * other.imaginary + self.imaginary * other.real)
        else:
            return MyComplex(self.real * other, self.imaginary * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        return self + -1 * other

    def __rsub__(self, other):
        return -1 * self + other

    def __truediv__(self, other):
        if (isinstance(other, MyComplex)):
            return self * other.inverse()
        else:
            return MyComplex(self.real / other, self.imaginary / other)

    def __rtruediv__(self, other):
        return self.inverse() * other

    def __invert__(self):
        return self.conj()

    def __abs__(self):
        return self.magnitude()

    def __eq__(self, other):
        return (self.real == other.real and self.imaginary == other.imaginary) or \
               (abs(self.real - other.real) < TOLERANCE and abs(self.imaginary - other.imaginary) < TOLERANCE)