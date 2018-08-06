from project.models import *
import geonamescache

gc = geonamescache.GeonamesCache()
cities_dict = gc.get_cities()

if len(City.query.all())==0:
	our_cities = []
	for i in cities_dict:
		if cities_dict[i]['countrycode'] == "IL" or cities_dict[i]['countrycode'] == "PS":
			our_cities.append((cities_dict[i]['name'],cities_dict[i]['countrycode']))
	our_cities.sort()
	for c in our_cities:
		city = City()
		city.city = c[0]
		print(c[0])
		city.country = c[1]
		db.session.add(city)
		db.session.commit()
		print("successful")
		print(len(City.query.all()))
	print("Done!")
else:
	print(len(City.query.all()))
	print("Built already!")