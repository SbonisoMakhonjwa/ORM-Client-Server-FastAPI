from fastapi import FastAPI
from fire_station_distance_calculator import process_fire_stations
from datetime import datetime

app = FastAPI()


@app.get("/coordinates/fireStations")
def get_fire_station_location_for_coords(longitude:float,latitude:float):
    print('/coordinates/fireStations request received: ',datetime.now(),'longitude:',longitude,'latitude',latitude)
    response =  process_fire_stations(longitude,latitude)
    print('/coordinates/fireStations response returned: ',datetime.now(),'longitude:',longitude,'latitude',latitude)
    return response

