from project.models import *
import geonamescache

gc = geonamescache.GeonamesCache()
cities_dict = gc.get_cities()

if len(City.query.all())<0:
	for i in cities_dict:
		if cities_dict[i]['countrycode'] == "IL" or cities_dict[i]['countrycode'] == "PS":
			print(cities_dict[i]['name'])
			city = City()
			city.city = cities_dict[i]['name']
			city.country = cities_dict[i]['countrycode']
			db.session.add(city)
			db.session.commit()
			print("successful")
		print(len(City.query.all()))
	print("Done!")
else:
	print("Built already!")