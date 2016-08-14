## Matt Moehr
## 2016-08-14

## My pip/python 2/3 was a little jacked.
## downloaded: https://bootstrap.pypa.io/get-pip.py
## > sudo python2 get-pip.py
## > sudo pip2 install overpy

import overpy
import json
from urllib2 import urlopen

from collections import OrderedDict
from datetime import datetime
from decimal import Decimal
from xml.sax import handler, make_parser
import json
import re
import sys

api_url = "http://overpass-api.de/api/interpreter"

query = """
[out:json];
(
  area
    ["name"="Dane County"]
    ["admin_level"="6"]
    ["boundary"="administrative"];
)->.dane_county_boundary;
(
  way
    ["cycleway"~".*"]
    (area.dane_county_boundary);
);
out;"""

query = query.encode("utf-8")

conn = urlopen(api_url, query)

data = conn.read()

parsed = json.loads(data, parse_float = Decimal)

elements = parsed.get("elements", [])

'''
with open('../data/osm_bike_paths.json', 'w') as outfile:
    json.dump(data, outfile)

print(parsed)
'''

print(elements) 


'''

api = overpy.Overpass()

# fetch all ways and nodes
result = api.query("""
                    way(50.746,7.154,50.748,7.157) ["highway"];
                    (._;>;);
                    out body;
                   """)





## print results to the console
for way in result.ways:
    print("Name: %s" % way.tags.get("name", "n/a"))
    print("  Highway: %s" % way.tags.get("highway", "n/a"))
    print("  Nodes:")
    for node in way.nodes:
        print("    Lat: %f, Lon: %f" % (node.lat, node.lon))
'''

