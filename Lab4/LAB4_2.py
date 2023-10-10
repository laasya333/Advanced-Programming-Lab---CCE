import math
import cmath

n_str = input('Enter a complex number in the format a+bj: ')

n_complex = complex(n_str) #input string parsed to complex number

p_sin = math.sin(n_complex.real) * math.cosh(n_complex.imag) + 1j * (math.cos(n_complex.real) * math.sinh(n_complex.imag))
print("Sine of Complex Number:", p_sin)

p_log = math.log(abs(n_complex)) + 1j * math.atan2(n_complex.imag, n_complex.real)
print("log of Complex Number:", p_log)

p_sqrt = cmath.sqrt(n_complex)
print("Square Root of Complex Number:", p_sqrt)
