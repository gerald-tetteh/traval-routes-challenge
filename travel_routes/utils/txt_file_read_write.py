"""
Author: Gerald Addo-Tetteh
Text file read and write

This util file contains functions
that read from input file and 
write the available travel routes in
the output file
"""

def read_input(input_file_name):
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