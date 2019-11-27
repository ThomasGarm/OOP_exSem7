

from city import *

Lille = city("Lille", 59)
Lyon = city("Lyon", 69)
Paris = city("Paris", 92)
Strasbourg = city("Strasbourg", 67)
Brest = city("Brest", 29)
Roubaix = city("Roubaix", 59100)

print(Lille.show_location())
print(Lyon.show_location())
print(Paris.show_location())
print(Strasbourg.show_location())
print(Brest.show_location())

print(Roubaix.change_location())