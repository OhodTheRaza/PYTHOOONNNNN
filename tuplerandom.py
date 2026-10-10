import math
rainy = 0
sunny = 0
tuple1 = (1, 0, 0, 0, 1, 1, 0)
def weatherprediction(tuples):
    tuples.randint(1,7)
    if tuples == 1 > 0:
       rainy = rainy + 1
    else: 
       sunny = sunny + 1
weatherprediction(tuple1)
if rainy > sunny:
   prediction = rainy
else: 
   prediction  = sunny