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
s = input("What are wwe converting? ")
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
            Unit('oz', ['kg', 'gm', 'mg', 'lbs'], [0.0283495, 28.3495, 28349.5, 0.0625])]:
      if from_.endswith(i.unitname):
          val = float(from_.removesuffix(i.unitname))
          ind = i.convertsto.index(to_)
          print(val * i.conversionfactor[ind])
convert(s)
