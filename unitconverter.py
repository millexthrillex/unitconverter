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
s = input("Convertion format ie. '1kg to gm' \n")
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
            Unit('US gal', ['lt', 'ml', 'q', 'p', 'c', 'fl oz', 'tbsp', 'tsp', 'imp gal','imp q', 'imp p', 'imp fl oz','imp tbsp', 'imp tsp'], [3.78754, 3785.41, 4, 8, 16, 128, 256, 768, .8327, 3.3301, 6.6614, 133.2278, 639.4935]),
            Unit('US q', ['lt', 'ml', 'gal', 'p', 'c', 'fl oz', 'tbsp', 'tsp', 'imp gal','imp q', 'imp p', 'imp fl oz','imp tbsp', 'imp tsp'], [0.9464, 946.3525, .25, 2, 4, 32, 64, 192, .2082, .8327, 1.6653, 33.3069, 53.8734, 159.8734]),
            Unit('imp gal', ['ml', 'US gal', 'q', 'p', 'c', 'fl oz', 'tbsp', 'tsp', 'lt','imp q', 'imp p', 'imp fl oz','imp tbsp', 'imp tsp'], [4546.09, 1.201, 4.804, 9.608, 19.215, 153.7217, 307.443, 922.329977, 4.546, 4, 8, 160, 256, 768]),
            Unit('imp q', ['ml', 'US gal', 'q', 'p', 'c', 'fl oz', 'tbsp', 'tsp', 'imp gal', 'lt', 'imp p', 'imp fl oz', 'imp tbsp', 'imp tsp'], [1136.523, 0.3002, 1.201, 2.4019, 4.8038, 38.4304, 76.8608, 230.5825, 0.25, 1.1365, 2, 40, 64, 192]),
            Unit('imp p', ['ml', 'US gal', 'q', 'p', 'c', 'fl oz', 'tbsp', 'tsp', 'imp gal','imp q', 'lt', 'imp fl oz','imp tbsp', 'imp tsp'], [568.2613, 0.1501, 0.6005, 1.20095, 2.4019, 19.2152, 38.4304, 115.29125, 0.125 , 0.5, 0.5683, 20, 32, 96]),
            Unit('imp tbsp', ['ml', 'US gal', 'q', 'p', 'c', 'fl oz', 'tbsp', 'tsp', 'imp gal','imp q', 'imp p', 'lt','imp tsp', 'imp fl oz'], [17.7582, 0.00469, 0.01876, 0.03753, 0.07506, 0.60048, 1.20095, 3.6029, 0.0039, 0.0156, 0.03125, 0.01776, 3, 0.625]),
            Unit('imp tsp', ['ml', 'US gal', 'q', 'p', 'c', 'fl oz', 'tbsp', 'tsp', 'imp gal','imp q', 'imp p', 'imp fl oz','imp tbsp', 'lt'], [5.9194, 0.00156, 0.006255, 0.01251, 0.02502, 0.20016, 0.40032, 1.20095, 0.0013, 0.00521, 0.01042, 0.20833, 0.33333, 0.00592]),
            Unit('imp fl oz1', ['ml', 'US gal', 'q', 'p', 'c', 'fl oz', 'tbsp', 'tsp', 'imp gal','imp q', 'imp p', 'imp tbsp','lt', 'imp tsp'], [28.41306, 0.00751, 0.03002, 0.06005, 0.1201, 0.96076, 1.92152, 5.76456, 0.00625, 0.025, 0.05, 1.6, 0.02841, 4.8])]:
      
    if from_.endswith(i.unitname):
          val = float(from_.removesuffix(i.unitname))
          ind = i.convertsto.index(to_)
          result = val * i.conversionfactor[ind]
          fresult = f'{result:.3f}'
          print(fresult)
convert(s)
