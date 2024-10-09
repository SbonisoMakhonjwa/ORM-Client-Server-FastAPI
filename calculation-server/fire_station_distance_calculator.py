import geopandas as gpd
import osrm

fire_station_locations = gpd.read_file("Fire_Station_V2.shp")
fire_station_locations.rename(columns={'lng': 'longitude', 'lat': 'latitude'}, inplace=True)  
osrm_server_host = 'http://osrm-server:5000'

def fetch_distance(osrm_client,client_coords,fire_station):
    fire_station_coords = (fire_station['longitude'], fire_station['latitude'])
    response = osrm_client.route(coordinates=[client_coords, fire_station_coords])
    distance_meters = response['routes'][0]['distance']
    return [fire_station['suburb'], distance_meters]
    

def process_fire_stations(longitude,latitude):
    
    distances = []
    
    client_coords = (longitude, latitude)
    
    osrm_client = osrm.Client(host=osrm_server_host)
    
    for fire_station in fire_station_locations.iterrows():
        fire_station_object = fire_station[1]
        response = fetch_distance(osrm_client,client_coords,fire_station_object)
        distances.append(response)        
        
    distances.sort(key=lambda x: x[1])
    return distances