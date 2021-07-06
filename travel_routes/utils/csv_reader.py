"""
Author: Gerald Addo-Tetteh
CSV Reader Util

This util file contains functions
that read data from: 
'airlines.csv' 'airports.csv' 'routes.csv'
"""
import csv

from travel_routes.models.Airline import Airline
from travel_routes.models.Airport import Airport
from travel_routes.models.RoutesGraph import RouteGraph, RouteNode

AIRLINES_FILE = "airlines.csv";
AIRPORTS_FILE = "airports.csv";
ROUTES_FILE = "routes.csv";

def extract_airlines() -> dict[str,Airline]:
    """Reads active airlines from 'AIRLINES_FILE'
    and retruns a dictionary of Airlines
    """
    airlines = {}
    with open(AIRLINES_FILE) as airlines_file:
        for airline_data in csv.reader(airlines_file):
            id = int(airline_data[0].strip())
            if(id < 0 or (airline_data[7] != "Y")):
                continue
            iata_code = airline_data[3].strip()
            location_code = iata_code
            if(len(iata_code) < 2):
                location_code = airline_data[4].strip() #icao code
            if(airlines.get(id) == None):
                airline = Airline(id,location_code)
                airlines[id] = airline
    return airlines
            
def extract_airports() -> dict[str,Airport]:
    """Reads all airports from 'AIRPORTS_FILE'
    and retruns a dictionary of Airports
    """
    airports = {}
    with open(AIRPORTS_FILE) as airports_file:
        for airport_data in csv.reader(airports_file):
            id = int(airport_data[0].strip())
            if(id < 0):
                continue
            city = airport_data[2].strip()
            country = airport_data[3].strip()
            if(len(city) < 1 or len(country) < 1):
                continue
            iata_code = airport_data[4].strip()
            location_code = iata_code
            if(len(iata_code) < 2):
                location_code = airport_data[5].strip() #icao code
            airport = Airport(id,location_code)
            airports[f"{city},{country}"] = airport
    return airports

def extract_routes(airlines) -> RouteGraph:
    """Reads available routes from 'ROUTES_FILE'
    and retruns a RouteGraph
    """
    route_graph = RouteGraph()
    with open(ROUTES_FILE) as routes_file:
        for route_data in csv.reader(routes_file):
            try:
                airline_id = int(route_data[1].strip())
                if(airlines.get(airline_id) == None):
                    continue
                source_airport_id = int(route_data[3].strip())
                destination_airport_id = int(route_data[5].strip())
                stops = int(route_data[7].strip())
                source_route_node = None
                destination_route_node = None
                # check of node already exists
                if(route_graph.get_node(destination_airport_id) == None):
                    destination_route_node = RouteNode(destination_airport_id)
                else:
                    destination_route_node = route_graph.get_node(destination_airport_id)

                if(route_graph.get_node(source_airport_id) == None):
                    source_route_node = RouteNode(source_airport_id)
                    route_graph.add_vertex(source_route_node,
                        destination_route_node)
                else:
                    source_route_node = route_graph.get_node(source_airport_id)
                
                route_graph.add_edge(source_route_node,
                    destination_route_node,airline_id,stops)
            except Exception:
                continue
    return route_graph