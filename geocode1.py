from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent = "geocode")

location = geolocator.geocode("121 N laSalle St, chicago")

print(location.latitude, location.longitude)


location2 = geolocator.geocode("40 avenue de l'amiral lemonnier, marly-le-roi, FR")
print(location2.latitude, location2.longitude)
