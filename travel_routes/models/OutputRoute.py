"""
Author: Gerald Addo-Tetteh
OutputROute Class

This class represents the route
from source to destination. Incliding
any additional stops
"""

class OutputRoute:
    def __init__(self,airline_code,source_airport_code,
        destination_airport_code,stops) -> None:
        """Represents route"""
        self._airline_code = airline_code
        self._source_airport_code = source_airport_code
        self._destination_airport_code = destination_airport_code
        self._stops = stops
    
    def __repr__(self) -> str:
        return f"{self._airline_code} from {self._source_airport_code} " \
            f"to {self._destination_airport_code} {self._stops} stops"