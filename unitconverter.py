# This is the beginning of the file that Elliot went through in class
#
# Project Requirements:
#	Able to convert between common metric and Imperial cooking units of measure including mass, volume (liquid and bulk),
#	and temperature.
#	Eggs to cups
#	Kg to lbs
#	Tsp to cups
#
#	Tsp, Tbsp, Cups, Pints, Quarts, Fl. Oz., Lbs, Gal, Oz, Kg, G, L, mL, Farenheit, Celsius, Kelvin
#
#	Command-Line Interface
#		"Convert 6 tbsp to cups"
#		"7.2 Kg to lbs"
#
#
#
s = input("What are we converting? ")
class Unit:
  def __init__(self, unitname, convertsto, conversionfactor):
    self.unitname = unitname
    self.convertsto = convertsto
    self.conversionfactor = conversionfactor
def convert(s):
  [from_, to_] = s.split(' to ')
  for i in [Unit('kg', ['lbs', 'gm', 'mg', 'oz'], [2.2046244202, 1000, 1000000, 35.273990723]),
            Unit('lbs', ['oz', 'kg', 'gm', 'mg'], [16, 0.453592, 452.592, 453592]),
            Unit('gm', ['kg', 'mg', 'lbs', 'oz'], [0.001, 1000, 0.0022046244, 0.0352739907]),
            Unit('mg', ['kg', 'gm', 'lbs', 'oz'], [0.000001, 0.001, 0.0000022046, 0.000035274]),
            Unit('oz', ['kg', 'gm', 'mg', 'lbs'], [0.0283495, 28.3495, 28349.5, 0.0625]),
            
            Unit('c', ['k', 'f'], [274.15, 33.8]),
            Unit('k', ['c', 'f'], [-272.15, -457.87]),
            Unit('f', ['c', 'k'], [-17.2, 255.93]),
            
            Unit('lt', ['ml', 'gal', 'q', 'p', 'c', 'fl oz', 'tbsp', 'tsp', 'imp gal','imp q', 'imp p', 'imp fl oz','imp tbsp', 'imp tsp'], [1000, .2642, 1.0567, 2.1134, 4.2267, 33.8140, 67.6280, 202.8842, .2199, .8799, 1.7598, 35.1951, 56.3121, 168.9364]),
            Unit('ml', ['lt', 'gal', 'q', 'p', 'c', 'fl oz', 'tbsp', 'tsp', 'imp gal','imp q', 'imp p', 'imp fl oz','imp tbsp', 'imp tsp'], [.001, .00026, .0011, .0021, .0042, .0338, .0676, .2029, .0002, .0008, .0018, .0352, .0563, .1689]),
            Unit('gal', ['lt', 'ml', 'q', 'p', 'c', 'fl oz', 'tbsp', 'tsp', 'imp gal','imp q', 'imp p', 'imp fl oz','imp tbsp', 'imp tsp'], [3.78754, 3785.41, 4, 8, 16, 128, 256, 768, .8327, 3.3301, 6.6614, 133.2278, 639.4935]),
            Unit('q', ['lt', 'ml', 'gal', 'p', 'c', 'fl oz', 'tbsp', 'tsp', 'imp gal','imp q', 'imp p', 'imp fl oz','imp tbsp', 'imp tsp'], [.9464, 946.3525, .25, 2, 4, 32, 64, 192, .2082, .8327, 1.6653, 33.3069, 53.8734, 159.8734])]:
      
    if from_.endswith(i.unitname):
          val = float(from_.removesuffix(i.unitname))
          ind = i.convertsto.index(to_)
          print(val * i.conversionfactor[ind])
convert(s)
