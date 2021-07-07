"""
Author: Gerald Addo-Tetteh
__init__ file
"""

from travel_routes.utils.txt_file_read_write import read_input, write_to_file
from travel_routes.utils.csv_reader import read_files

def main(input_file) -> None:
    try:
      source,destination = read_input(input_file)
    except Exception:
      print(f"An error occurred, check file path '{input_file}' "\
          "or contents")
      return
    airlines,route_graph,airports,airports_alias = read_files()
    source_node = route_graph.get_node(airports[source].id)
    destination_node = route_graph.get_node(airports[destination].id)
    result = None
    if(source_node != None and destination_node != None):
        result = route_graph.get_route(source_node,destination_node)
    write_to_file(input_file,result,
        route_graph,airlines,airports,airports_alias)