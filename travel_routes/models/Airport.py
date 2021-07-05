"""
Author: Gerald Addo-Tetteh
Airport Class
"""

class Airport:
    def __init__(self,id,iata_code,icao_code) -> None:
        """Class to represent an Airport"""
        self._id = id
        self._iata_code = iata_code
        self._icao_code = icao_code
    
    @property
    def id(self) -> int:
        """Returns airport ID"""
        return self._id
    
    @property
    def iata_code(self) -> str:
        """Returns airport IATA code"""
        return self._iata_code
    
    @property
    def icao_code(self) -> str:
        """Retruns airport ICAO code"""
        return self._icao_code