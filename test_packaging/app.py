from txt_analyser import Gen, Clean, Order

g = Gen()
c = Clean(g.generate())
o = Order(c.process())
print(o.getOccurences(20))