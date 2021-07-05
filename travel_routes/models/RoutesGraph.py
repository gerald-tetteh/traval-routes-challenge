"""
Author: Gerald Addo-Tetteh
RouteGraph Class

This class contains a graph of
all possible routes for source
to destination
"""
from collections import defaultdict

class RouteNode:
    def __init__(self,location_code) -> None:
        self._location_code = location_code
    
    @property
    def location_code(self):
        return self._location_code

class RouteGraph:
    def __init__(self) -> None:
        """A class representing the routes graph"""
        self.number_of_nodes = 0
        self.adjacent_nodes = defaultdict(lambda: False)
    
    def _add_edge(self,node,airline_id) -> None:
        """Adds Edge to existing node"""
        self.adjacent_nodes[node].append([node,airline_id])
    
    def add_vertex(self,node,airline_id) -> None:
        """Add a location to the graph

        Args:
            node: A Route Node
        """
        if(not self.adjacent_nodes[node]):
            self.adjacent_nodes[node] = []
        else:
            self._add_edge(node, airline_id)
