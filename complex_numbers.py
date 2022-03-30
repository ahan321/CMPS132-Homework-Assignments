class Complex:

    def __init__(self,r,i):
        self._real = r
        self._imag = i

    def __str__(self):
        if self._imag>=0:
           return f"{self._real} + {self._imag}i"
        else:
           return f"{self._real} - {abs(self._imag)}i"

    def conjugate(self):
        ans = Complex(self._real, -1*self._imag)
        return ans

    def __mul__(self,other):
        if isinstance(other, Complex):
            real_part = self._real*other._real-self._imag*other._imag
            imag_part = self._real*other._imag+self._imag*other._real
            ans = Complex(real_part, imag_part)
        else:
            ans = Complex(self._real*other, self._imag*other)
        return ans

    def __rmul__(self,other):
        return self * other
    
    def __eq__(self, other):
        if self._real == other._real and self._imag == other._imag:
            return True
        return False

class Real(Complex):
    def __init__(self, value):
        super().__init__(value,0)
    def __int__(self):
        return int(self._real)
    def __float__(self):
        return float(self._real)
    
def lah(a,b):
    a = a + z
    return a

