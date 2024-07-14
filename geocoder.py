from geopy.geocoders import Nominatim
from geopy import distance


geocoder=Nominatim(user_agent="i know python")
location1="chennai"
location2="delhi"

coordinates1=geocoder.geocode(location1)
coordinates2=geocoder.geocode(location2)

lat1,long1=(coordinates1.latitude),(coordinates1.longitude)
lat2,long2=(coordinates2.latitude),(coordinates2.longitude)

place1=(lat1,long1)
place2=(lat2,long2)

print(distance.distance(place1,place2))
def distance(location1,location2):
    geocoder=Nominatim(user_agent="i know python")
    coordinates1=geocoder.geocode(location1)
    coordinates2=geocoder.geocode(location2)

    lat1,long1=(coordinates1.latitude),(coordinates1.longitude)
    lat2,long2=(coordinates2.latitude),(coordinates2.longitude)

    place1=(lat1,long1)
    place2=(lat2,long2)

    return distance.distance(place1,place2)


        


        


                        
