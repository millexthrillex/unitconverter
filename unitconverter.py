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




class Unit:
  def __init__(self, unitname, convertsto, conversionfactor):
    self.unitname = unitname
    self.convertsto = convertsto
    self.conversionfactor = conversionfactor

def _m(factor): return lambda v: v * factor

def _a(factor): return lambda v: v + factor

def convert(s):
  
  [from_, to_] = s.split(' to ')
  
Unit.conversions = [Unit('kg', ['lbs', 'gm', 'mg', 'ozs'], [_m(2.2046244202), _m(1000), _m(1000000), _m(35.273990723)]),
                    Unit('lbs', ['ozs', 'kg', 'gm', 'mg'], [_m(16), _m(0.453592), _m(452.592), _m(453592)]),
                    Unit('gm', ['kg', 'mg', 'lbs', 'ozs'], [_m(0.001), _m(1000), _m(0.0022046244), _m(0.0352739907)]),
                    Unit('mg', ['kg', 'gm', 'lbs', 'ozs'], [_m(0.000001), _m(0.001), _m(0.0000022046), _m(0.000035274)]),
                    Unit('ozs', ['kg', 'gm', 'mg', 'lbs'], [_m(0.0283495), _m(28.3495), _m(28349.5), _m(0.0625)]),
            
                    Unit('cel', ['f', 'k'], [ lambda c: c * 1.8 + 32, _a(237.15)]),
                    Unit('k', ['cel', 'f'], [_a(-273.15), lambda f: (f - 273.15) * 1.8 + 32]),
                    Unit('f', ['cel', 'k'], [lambda f: (f - 32) * .556, lambda k: ((k -32) * .556) - 273.15]),
                    
                    Unit('imp gal', ['ml', 'us gal', 'us q', 'us p', 'c', 'us fl oz', 'us tbsp', 'us tsp', 'lt','imp q', 'imp p', 'imp fl oz','imp tbsp', 'imp tsp'], [_m(4546.09), _m(1.201), _m(4.804), _m(9.608), _m(19.215), _m(153.7217), _m(307.443), _m(922.329977), _m(4.546), _m(4), _m(8), _m(160), _m(256), _m(768)]),
                    Unit('imp q', ['ml', 'us gal', 'us q', 'us p', 'c', 'us fl oz', 'us tbsp', 'us tsp', 'imp gal', 'lt', 'imp p', 'imp fl oz', 'imp tbsp', 'imp tsp'], [_m(1136.523), _m(0.3002), _m(1.201), _m(2.4019), _m(4.8038), _m(38.4304), _m(76.8608), _m(230.5825), _m(0.25), _m(1.1365), _m(2), _m(40), _m(64), _m(192)]),
                    Unit('imp p', ['ml', 'us gal', 'us q', 'us p', 'c', 'us fl oz', 'us tbsp', 'us tsp', 'imp gal','imp q', 'lt', 'imp fl oz','imp tbsp', 'imp tsp'], [_m(568.2613), _m(0.1501), _m(0.6005), _m(1.20095), _m(2.4019), _m(19.2152), _m(38.4304), _m(115.29125), _m(0.125), _m(0.5), _m(0.5683), _m(20), _m(32), _m(96)]),
                    Unit('imp tbsp', ['ml', 'us gal', 'us q', 'us p', 'c', 'us fl oz', 'us tbsp', 'us tsp', 'imp gal','imp q', 'imp p', 'lt','imp tsp', 'imp fl oz'], [_m(17.7582), _m(0.00469), _m(0.01876), _m(0.03753), _m(0.07506), _m(0.60048), _m(1.20095), _m(3.6029), _m(0.0039), _m(0.0156), _m(0.03125), _m(0.01776), _m(3), _m(0.625)]),
                    Unit('imp tsp', ['ml', 'us gal', 'us q', 'us p', 'c', 'us fl oz', 'us tbsp', 'us tsp', 'imp gal','imp q', 'imp p', 'imp fl oz','imp tbsp', 'lt'], [_m(5.9194), _m(0.00156), _m(0.006255), _m(0.01251), _m(0.02502), _m(0.20016), _m(0.40032), _m(1.20095), _m(0.0013), _m(0.00521), _m(0.01042), _m(0.20833), _m(0.33333), _m(0.00592)]),
                    Unit('imp fl oz', ['ml', 'us gal', 'us q', 'us p', 'c', 'us fl oz', 'us tbsp', 'us tsp', 'imp gal','imp q', 'imp p', 'imp tbsp','lt', 'imp tsp'], [_m(28.41306), _m(0.00751), _m(0.03002), _m(0.06005), _m(0.1201), _m(0.96076), _m(1.92152), _m(5.76456), _m(0.00625), _m(0.025), _m(0.05), _m(1.6), _m(0.02841), _m(4.8)]),
                    
                    Unit('lt', ['ml', 'us gal', 'us q', 'us p', 'c', 'us fl oz', 'us tbsp', 'us tsp', 'imp gal','imp q', 'imp p', 'imp fl oz','imp tbsp', 'imp tsp'], [_m(1000), _m(0.2642), _m(1.0567), _m(2.1134), _m(4.2267), _m(33.8140), _m(67.6280), _m(202.8842), _m(0.2199), _m(0.8799), _m(1.7598), _m(35.1951), _m(56.3121), _m(168.9364)]),
                    Unit('ml', ['lt', 'us gal', 'us q', 'us p', 'c', 'us fl oz', 'us tbsp', 'us tsp', 'imp gal','imp q', 'imp p', 'imp fl oz','imp tbsp', 'imp tsp'], [_m(0.001), _m(0.00026), _m(0.0011), _m(0.0021), _m(0.0042), _m(0.0338), _m(0.0676), _m(0.2029), _m(0.0002), _m(0.0008), _m(0.0018), _m(0.0352), _m(0.0563), _m(0.1689)]),
                    Unit('us gal', ['lt', 'ml', 'us q', 'us p', 'c', 'us fl oz', 'us tbsp', 'us tsp', 'imp gal','imp q', 'imp p', 'imp fl oz','imp tbsp', 'imp tsp'], [_m(3.78754), _m(3785.41), _m(4), _m(8), _m(16), _m(128), _m(256), _m(768), _m(0.8327), _m(03.3301), _m(06.6614), _m(0133.2278), _m(0639.4935)]),
                    Unit('us q', ['lt', 'ml', 'us gal', 'us p', 'c', 'us fl oz', 'us tbsp', 'us tsp', 'imp gal','imp q', 'imp p', 'imp fl oz','imp tbsp', 'imp tsp'], [_m(0.9464), _m(946.3525), _m(0.25), _m(2), _m(4), _m(32), _m(64), _m(192), _m(.2082), _m(.8327), _m(1.6653), _m(33.3069), _m(53.8734), _m(159.8734)]),
                    Unit('us p', ['lt', 'ml', 'us gal', 'c', 'us fl oz', 'us tbsp', 'us tsp', 'imp gal','imp q', 'imp p', 'imp fl oz','imp tbsp', 'imp tsp'], [_m(0.4732), _m(473.1763), _m(0.125), _m(0.5), _m(2), _m(16), _m(32), _m(96), _m(0.1), _m(0.4163), _m(0.8327), _m(16.6534), _m(26.6456), _m(79.9367)]),
	            Unit('c', ['eggs','lt', 'ml', 'us gal', 'us q', 'us p', 'us fl oz', 'us tbsp', 'us tsp', 'imp gal','imp q', 'imp p', 'imp fl oz','imp tbsp', 'imp tsp'], [_m(4), _m(0.2366), _m(236.5881), _m(0.0625), _m(0.25), _m(0.5), _m(8), _m(16), _m(48), _m(0.05204), _m(0.2082), _m(0.4164), _m(8.3267), _m(13.3228), _m(39.9683)]),
	            Unit('us fl oz', ['lt', 'ml', 'us gal', 'us q', 'us p', 'c', 'us tbsp', 'us tsp', 'imp gal','imp q', 'imp p', 'imp fl oz','imp tbsp', 'imp tsp'], [_m(0.02957), _m(29.5735), _m(0.0078), _m(.0313), _m(.0625), _m(.125), _m(2), _m(6), _m(0.0065), _m(0.0260), _m(0.0520), _m(1.0408), _m(1.6653), _m(4.9960)]),
	            Unit('us tbsp', ['lt', 'ml', 'us gal', 'us q', 'us p', 'c', 'us fl oz', 'us tsp', 'imp gal','imp q', 'imp p', 'imp fl oz','imp tbsp', 'imp tsp'], [_m(0.0148), _m(14.7868), _m(0.0039), _m(0.0156), _m(0.0312), _m(0.0625), _m(0.5), _m(3), _m(0.0033), _m(0.01310), _m(0.0260), _m(0.5204), _m(0.83287), _m(2.498)]),
	            Unit('us tsp', ['lt', 'ml', 'us gal', 'us q', 'us p', 'c', 'us fl oz', 'us tbsp', 'imp gal','imp q', 'imp p', 'imp fl oz','imp tbsp', 'imp tsp'], [_m(0.0049), _m(4.9289), _m(.0013), _m(.0052), _m(.0104), _m(0.0208), _m(0.1667), _m(0.3333), _m(0.0012), _m(0.0043), _m(0.0086), _m(0.1735), _m(0.2776), _m(0.8327)]),

                    Unit('eggs', ['c'], [_m(0.25)])]


def convert(s):
  [from_, to_] = s.split(' to ')
  for i in Unit.conversions:
    if from_.endswith(i.unitname):
      val = float(from_.removesuffix(i.unitname))
      ind = i.convertsto.index(to_)
      res = i.conversionfactor[ind](val)
      print(from_, "is", f'{res:.3f}{i.convertsto[ind]}')


if __name__ == "__main__":
  while True:
    s = input("Please enter what you would like to convert. \n(Conversion format ie. '1kg to gm') \n")

    convert(s)

    x = input("Press any key to continue, 'q' to exit ")

    if x == "q":

      break
