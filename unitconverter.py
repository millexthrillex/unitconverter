#This is the beginning of the file that Elliot went through in class
#
#
#
#
#

class Unit:
  def __init__(self, unitname, convertsto, conversionfactor):
    self.unitname = unitname
    self.convertsto = convertsto
    self.conversionfactor = conversionfactor

def convert(s):
  [from_, to_] = s.split(' to ')

  for i in [Unit('kg', ['lbs', 'g'], [2.205, 1000]),
            Unit('lbs', ['oz', 'kg'], [16, 1 / 2.205])]:
      if from_.endswith(i.unitname):
          val = float(from_.removesuffix(i.unitname))
          ind = i.convertsto.index(to_)
          print(val * i.conversionfactor[ind])

convert("7.2kg to lbs")
convert("3lbs to oz")
convert("7.2kg to g")
