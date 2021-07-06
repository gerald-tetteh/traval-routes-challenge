"""
Author: Gerald Addo-Tetteh
__init__ file
"""

from travel_routes.utils.txt_file_read_write import read_input
from travel_routes.utils.csv_reader import read_files

def main(input_file):
    try:
      source,destination = read_input(input_file)
    except Exception:
      print(f"File could not be open, check path {input_file}")
      return
    airlines,route_graph,airports = read_files()
    source_node = route_graph.get_node(airports[source].id)
    destination_node = route_graph.get_node(airports[destination].id)
    result = route_graph.get_route(source_node,destination_node)