"""
Author: Gerald Addo-Tetteh
Text file read and write

This util file contains functions
that read from input file and 
write the available travel routes in
the output file
"""

from travel_routes.models.OutputRoute import OutputRoute

def read_input(input_file_name) -> list:
    """Reads the source and destination
    city,country from the input file. Retruns a
    list containing formated strings made from the 
    locations

    Args:
        input_file_name: Name of input file
    """
    source_destination = []
    with open(input_file_name) as input_file:
        for row in input_file:
            city_country = row.split(",")
            source_destination.append(f"{city_country[0]},{city_country[1]}"
                .strip())
    return source_destination

def get_airport_code(airport_alias,airports,airport_id) -> str:
    """Returns either the IATA or ICAO code
    that corresponds to the airport_id

    Args:
        airport_alias: Dictionary(keys: airport_id, values: airport_keys)
        airports: Contains available airports
        airport_id: Airport ID
    """
    key = airport_alias.get(airport_id)
    return airports.get(key).location_code

def write_to_file(input_file_name,routes,
    route_graph,airlines,airports,airports_alias) -> None:
    """Writes optimal route if available from source
    to destination.

    Args:
        input_file_name: Name of input file
        routes: Optimal route if available else None
        route_graph: Graph of all the routes
        airlines: Dictionary containing active airlines
        airports: Dictionary containing available airports
        airports_alias: Dictionary(keys: airport_id, values: airport_keys)
    """
    output_file_name = input_file_name.split(".txt")[0] + "_output.txt"
    with open(output_file_name, mode="w") as output_file:
        if (routes == None):
            return
        for i in range(0,len(routes) - 1):
            key = f"{routes[i]},{routes[i+1]}"
            airline_id,stops = route_graph.get_connection(key)
            airline_code = airlines.get(airline_id
                ).location_code
            source_airport_code = get_airport_code(airports_alias,
                airports,routes[i].airport_id)
            destination_airport_code = get_airport_code(airports_alias,
                airports,routes[i+1].airport_id)
            route = OutputRoute(airline_code,
                source_airport_code,destination_airport_code,stops)
            output_file.write(f"{route}\n")
    return