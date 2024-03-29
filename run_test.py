#from dias.scripts.simulate_model import *
from simulate_model import *
import time
#start_time = time.time()

def run_flood(file, user_min, user_max):	
	"""
	This begins the example use case of value_impact_analysis
	
	"""
	# Begin with dBase file commonly associated with attribute data for annotating layers in a GIS
	file = "static/upload/AB_HOQ_DATA.dbf"
	print("GETTIN ELEVATIONS")
	#file = file
	# Open the file and intitialize the flood model class
	print("gettin them elevations")
	elevations = "elevations.csv"
	
	
	# Define the column or id names
	# These will be hard coded and should not be allowed to change
	lat = 'Lat'
	lon = 'Long'
	building_value_field = 'BLDGVALUE'
	land_value_field = 'LANDVALUE'
	parcel_field = 'PARCELATT'
	impact_field = "Impact_Zones_12"
	output_file_name = 'output.csv'
	impact_range = (user_min, user_max)
	#max_impact = 14
	max_impact = user_max
	time_step = 25
	iterations = 500
	impact_multiplier = 0.8
	
	if (file == None or elevations == None or max_impact == None):
		print("file or elev or maximpact none!")
	else:
		print("ALL THINGS")
	model = build_base_model(file, elevations, lat, lon, max_impact, impact_multiplier)
	print(model)
	
	sim = simulate_base_model(model, building_value_field, land_value_field, impact_range, iterations, time_step, output_file_name)
	
	zones = impact_by_zone(sim, parcel_field, impact_field)
	print(zones)
	
	#print("took ", time.time() - start_time, "to run")
	# run_model(file, elevations, lat, lon,  building_value_field, land_value_field, parcel_field, impact_field, impact_range, max_impact, impact_multiplier, iterations, time_step, output_file_name)
	return
