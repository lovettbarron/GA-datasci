from __future__ import division
from collections import Counter, defaultdict
from functools import partial
import math, random, csv
import matplotlib.pyplot as plt
import dateutil.parser

#
#
# From book
#
#

# Returns a 
def parse_dict(input_dict, parser_dict):
    return { field_name : try_parse_field(field_name, value, parser_dict)
            for field_name, value in input_dict.iteritems() }

def parse_row(input_row, parsers):
    """given a list of parsers (some of which may be None)
    apply the appropriate one to each element of the input_row"""
    return [parser(value) if parser is not None else value
        for value, parser in zip(input_row, parsers)]

def parse_rows_with(reader, parsers):
    """wrap a reader to apply the parsers to each of its rows"""
    for row in reader:
        yield parse_row(row, parsers)

#
#
# My stuff
#
#

if __name__ == "__main__":
    random.seed()

    data = []

    with open("data/SFPD_Incidents_-_Previous_Three_Months.csv","rb") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for line in parse_rows_with(reader, [dateutil.parser.parse, None, float]):
            data.append(line)