a = "Carlo Jose Luis"
n = len(a)
print("Longitud:", n)
print("a[0] =", a[0])
print("a[n-1] =", a[n-1])
print("a[-1] =", a[-1])
print("a[-n] =", a[-n])
try:
    print("a[n] =", a[n])
except IndexError:
    print("a[n] produce un error: índice fuera de rango")

try:
    print("a[-n-1] =", a[-n-1])
except IndexError:
    print("a[-n-1] produce un error: índice fuera de rango")

try:
    print("a[1.5] =", a[1.5])
except TypeError:
    print("a[1.5] produce un error: el índice debe ser entero")

try:
    print("a[1.0] =", a[1.0])
except TypeError:
    print("a[1.0] produce un error: el índice debe ser entero")