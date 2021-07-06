"""
Author: Gerald Addo-Tetteh
RouteGraph Class

This class contains a graph of
all possible routes for source
to destination
"""
from queue import Queue

class RouteNode:
    """Represents graph node"""
    def __init__(self,airport_id) -> None:
        self._airport_id = airport_id
    
    @property
    def airport_id(self) -> int:
        """Returns airport ID"""
        return self._airport_id

class RouteGraph:
    def __init__(self) -> None:
        """A class representing the routes graph"""
        self._route_connects = {}
        self._nodes = {}
        self._number_of_nodes = 0
        self._adjacent_nodes = {}
    
    def add_edge(self,source_node,
        destination_node,airline_id,stops) -> None:
        """Adds Edge to existing node

        Args:
            airline_id: ID of airline to node
            source_node: Node of source
            destination_node: Node of destination
            stops: Number of additional stops
        """
        self._adjacent_nodes[source_node].append(destination_node)
        self._route_connects[
            f"{source_node},{destination_node}"] = [airline_id,stops]
    
    def add_vertex(self,source_node,destination_node) -> None:
        """Add a location to the graph

        Args:
            source_node: Source RouteNode
            destination_node: Destination RouteNode
        """
        self._number_of_nodes += 1
        self._nodes[source_node.airport_id] = source_node
        self._nodes[destination_node.airport_id] = destination_node
        self._adjacent_nodes[source_node] = []

    def get_node(self, airport_id) -> RouteNode:
        """Returns node corresponding to
        airport ID

        Args:
            airport_id: Airport ID
        """
        return self._nodes.get(airport_id, None)
    
    def get_route(self,source,destination):
        """Retrun availabel routes from
        source to destination

        Args:
            source: Source node
            destination: Destination node
        """
        if(source == destination):
            return None
        visited = {}
        queue = Queue()
        queue.put([source])
        while not queue.empty():
            path = queue.get()
            node = path[-1]
            if(visited.get(node) == None):
                adjacent_nodes = self._adjacent_nodes.get(node)
                if(adjacent_nodes == None):
                    continue
                for adjacent_node in adjacent_nodes:
                    new_path = list(path)
                    new_path.append(adjacent_node)
                    queue.put(new_path)
                    if (adjacent_node == destination):
                        return new_path
                visited[node] = True
        return None