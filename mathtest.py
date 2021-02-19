import math as m

x=m.e

y_natural = m.log(x)
y_base10 = m.log(x, 10)
y_log10 = m.log10(x)

print(x, y_natural, y_base10, y_log10)

deg = 60

rads = deg * m.pi / 180
rads_fromfunc = m.radians(deg)

print(deg, m.pi, rads, rads_fromfunc)

deg = 180

cos_deg = m.cos(deg)
cos_rad = m.cos(m.radians(deg))

print(deg, cos_deg, cos_rad)

fac5 = m.factorial(5)

print(fac5)
