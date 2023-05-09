def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784
    miles = 100 / 1.609344

    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    kilometers = miles * 1.609344
    liters = 3.785411784

    return liters / kilometers * 100
    
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
