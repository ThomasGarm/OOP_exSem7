

from city import *

Lille = City("Lille", 59)
Lyon = City("Lyon", 69)
Paris = City("Paris", 92)
Strasbourg = City("Strasbourg", 67)
Brest = City("Brest", 29)
Roubaix = City("Roubaix", 59100)

print(Lille.show_location())
print(Lyon.show_location())
print(Paris.show_location())
print(Strasbourg.show_location())
print(Brest.show_location())
print(Roubaix.show_location())


print(Paris.change_location("Dunkerque", 59)) #None appear
print(Paris.show_location())