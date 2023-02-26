from geopy.geocoders import Nominatim

def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="myapp") # create a geolocator object
    location = geolocator.geocode(city_name) # retrieve the location data
    if location:
        return (location.latitude, location.longitude) # return the latitude and longitude as a tuple
    else:
        return None # if the location is not found, return None


city_name = "Istanbul"
coordinates = get_coordinates(city_name)
print(coordinates)
