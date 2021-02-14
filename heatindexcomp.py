from readdata import read_data
from printing import print_comparison

# Column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'humout':5,
           'heatindex':13}

# Data types for each column (only if non-string)
types = {'tempout': float, 'humout': float, 'heatindex': float}

# Read data from file
data = read_data(columns, types=types)

# Compute the heat index
def compute_heatindex(t, hum):
   a = -42.379
   b = 2.04901523
   c = 10.14333127
   d = -0.22475541
   e = -0.00683783
   f = -0.05481717
   g = 0.00122874
   h = 0.00085282
   i = -0.00000199

   rh = hum / 100

   hi = a + (b * t) + (c * rh) + (d * t * rh) \
      + (e * t**2) + (f * rh**2) + (g * t**2 * rh) \
      + (h * t * rh**2) + (i * t**2 * rh**2)
   return hi

# Running the function to compute headindex
heatindex = []
for temp, hum in zip(data['tempout'], data['humout']):
    heatindex.append(compute_heatindex(temp, hum))

# Output comparison of data
print_comparison('HEAT INDEX', data['date'], data['time'], data['heatindex'], heatindex)
