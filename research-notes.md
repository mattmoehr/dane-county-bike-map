
## Possible data munging flow

1. Python script to query OpenStreetMap's Overpass API.
  - Yay, there are lots of wrappers available.
    - overpy is most fleshed out https://python-overpy.readthedocs.io/en/latest/introduction.html
      - This thing makes a special Result class, which is great if you're keeping all the processing in python, but all I want to do is download json and upload geoJSON, so the Result class is just an unnecessary hassle.
      - I hacked on it a bit and grabbed just the query and save code -- skipping the parsing code -- and that could work, but seems a little gimmicky.
    - "thin wrapper" https://github.com/mvexel/overpass-api-python-wrapper
      - I like the thin wrapper better because it just spits out JSON.
      - Now I realize that I need geoJSON...
    - query-overpass https://github.com/perliedman/query-overpass
      - These seems better, but the heavy lifting of going from overpass's json to geoJSON is handled by geojsonio-cli; so that's just another dependency in the yak-shaving adventure. Sigh.
  - May need to have a separate query for each bike path type.
  - Look into ways to say, "is this result object exactly the same as the one I already have in the map?"
  - Stash files (json text files, I presume) on the server with the script.
2. Load data as a layer into a Mapbox. (API? Styling applied automatically?)
  - Does Mapbox have an API for uploading data? Can it be used to replace/update existing layers?
  - In a CartoCSS world, the new data would always get the style. Need to make sure that style stays the same with data updates.
  - 
3. Mapbox WebGL page.
  - Does this have to WebGL? Possible run as both Leaflet and WebGL?

## Notes on existing bike maps

### Mapbox

- https://github.com/mapbox/mapbox-studio-run-bike-and-hike.tm2
  - This is the old carto CSS but maybe informative for style tips?
- https://www.mapbox.com/help/overpass-turbo/
  - Helpful tutorial for bringing in OSM data.
  - What is Overpass Turbo? Maybe it's an API run by OSM?
  
### OpenStreetMap

- Details on bike features: http://wiki.openstreetmap.org/wiki/Bicycle
- Feature tag `cycleway=*`
- Besides the cycleway tag, also remember:
  - amenities for bike parking
  - barriers for bikes
  - `highway:footway` with `bicycle=yes`
  - `highway:path` with `highway=cycleway`
- Cycle routes: http://wiki.openstreetmap.org/wiki/Cycle_routes

### OpenCycleMap

- http://www.opencyclemap.org/
- These are rendered tiles. They seem to open for download, but they can not be styled. I think.

### National Park Service

- Tom Patterson (www.shadedrelief.com) makes awesome maps that are kind to the user.
- Here are some symbols from NPS https://www.nps.gov/hfc/carto/map-symbols.cfm


