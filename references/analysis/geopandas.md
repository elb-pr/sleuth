# GeoPandas

GeoPandas extends pandas to enable spatial operations on geometric types. It combines the capabilities of pandas and shapely for geospatial data analysis.

## Installation

```bash
uv pip install geopandas
```

### Optional Dependencies

```bash
# For interactive maps
uv pip install folium

# For classification schemes in mapping
uv pip install mapclassify

# For faster I/O operations (2-4x speedup)
uv pip install pyarrow

# For PostGIS database support
uv pip install psycopg2
uv pip install geoalchemy2

# For basemaps
uv pip install contextily

# For cartographic projections
uv pip install cartopy
```

## Quick Start

```python
import geopandas as gpd

# Read spatial data
gdf = gpd.read_file("data.geojson")

# Basic exploration
print(gdf.head())
print(gdf.crs)
print(gdf.geometry.geom_type)

# Simple plot
gdf.plot()

# Reproject to different CRS
gdf_projected = gdf.to_crs("EPSG:3857")

# Calculate area (use projected CRS for accuracy)
gdf_projected['area'] = gdf_projected.geometry.area

# Save to file
gdf.to_file("output.gpkg")
```

## Core Concepts

### Data Structures

- **GeoSeries**: Vector of geometries with spatial operations
- **GeoDataFrame**: Tabular data structure with geometry column

See [data-structures.md](references/data-structures.md) for details.

### Reading and Writing Data

GeoPandas reads/writes multiple formats: Shapefile, GeoJSON, GeoPackage, PostGIS, Parquet.

```python
# Read with filtering
gdf = gpd.read_file("data.gpkg", bbox=(xmin, ymin, xmax, ymax))

# Write with Arrow acceleration
gdf.to_file("output.gpkg", use_arrow=True)
```

See [data-io.md](references/data-io.md) for comprehensive I/O operations.

### Coordinate Reference Systems

Always check and manage CRS for accurate spatial operations:

```python
# Check CRS
print(gdf.crs)

# Reproject (transforms coordinates)
gdf_projected = gdf.to_crs("EPSG:3857")

# Set CRS (only when metadata missing)
gdf = gdf.set_crs("EPSG:4326")
```

See [crs-management.md](references/crs-management.md) for CRS operations.

## Common Operations

### Geometric Operations

Buffer, simplify, centroid, convex hull, affine transformations:

```python
# Buffer by 10 units
buffered = gdf.geometry.buffer(10)

# Simplify with tolerance
simplified = gdf.geometry.simplify(tolerance=5, preserve_topology=True)

# Get centroids
centroids = gdf.geometry.centroid
```

See [geometric-operations.md](references/geometric-operations.md) for all operations.

### Spatial Analysis

Spatial joins, overlay operations, dissolve:

```python
# Spatial join (intersects)
joined = gpd.sjoin(gdf1, gdf2, predicate='intersects')

# Nearest neighbor join
nearest = gpd.sjoin_nearest(gdf1, gdf2, max_distance=1000)

# Overlay intersection
intersection = gpd.overlay(gdf1, gdf2, how='intersection')

# Dissolve by attribute
dissolved = gdf.dissolve(by='region', aggfunc='sum')
```

See [spatial-analysis.md](references/spatial-analysis.md) for analysis operations.

### Visualization

Create static and interactive maps:

```python
# Choropleth map
gdf.plot(column='population', cmap='YlOrRd', legend=True)

# Interactive map
gdf.explore(column='population', legend=True).save('map.html')

# Multi-layer map
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
gdf1.plot(ax=ax, color='blue')
gdf2.plot(ax=ax, color='red')
```

See [visualization.md](references/visualization.md) for mapping techniques.

## Detailed Documentation

- **[Data Structures](references/data-structures.md)** - GeoSeries and GeoDataFrame fundamentals
- **[Data I/O](references/data-io.md)** - Reading/writing files, PostGIS, Parquet
- **[Geometric Operations](references/geometric-operations.md)** - Buffer, simplify, affine transforms
- **[Spatial Analysis](references/spatial-analysis.md)** - Joins, overlay, dissolve, clipping
- **[Visualization](references/visualization.md)** - Plotting, choropleth maps, interactive maps
- **[CRS Management](references/crs-management.md)** - Coordinate reference systems and projections

## Common Workflows

### Load, Transform, Analyze, Export

```python
# 1. Load data
gdf = gpd.read_file("data.shp")

# 2. Check and transform CRS
print(gdf.crs)
gdf = gdf.to_crs("EPSG:3857")

# 3. Perform analysis
gdf['area'] = gdf.geometry.area
buffered = gdf.copy()
buffered['geometry'] = gdf.geometry.buffer(100)

# 4. Export results
gdf.to_file("results.gpkg", layer='original')
buffered.to_file("results.gpkg", layer='buffered')
```

### Spatial Join and Aggregate

```python
# Join points to polygons
points_in_polygons = gpd.sjoin(points_gdf, polygons_gdf, predicate='within')

# Aggregate by polygon
aggregated = points_in_polygons.groupby('index_right').agg({
    'value': 'sum',
    'count': 'size'
})

# Merge back to polygons
result = polygons_gdf.merge(aggregated, left_index=True, right_index=True)
```

### Multi-Source Data Integration

```python
# Read from different sources
roads = gpd.read_file("roads.shp")
buildings = gpd.read_file("buildings.geojson")
parcels = gpd.read_postgis("SELECT * FROM parcels", con=engine, geom_col='geom')

# Ensure matching CRS
buildings = buildings.to_crs(roads.crs)
parcels = parcels.to_crs(roads.crs)

# Perform spatial operations
buildings_near_roads = buildings[buildings.geometry.distance(roads.union_all()) < 50]
```

## Performance Tips

1. **Use spatial indexing**: GeoPandas creates spatial indexes automatically for most operations
2. **Filter during read**: Use `bbox`, `mask`, or `where` parameters to load only needed data
3. **Use Arrow for I/O**: Add `use_arrow=True` for 2-4x faster reading/writing
4. **Simplify geometries**: Use `.simplify()` to reduce complexity when precision isn't critical
5. **Batch operations**: Vectorized operations are much faster than iterating rows
6. **Use appropriate CRS**: Projected CRS for area/distance, geographic for visualization

## Best Practices

1. **Always check CRS** before spatial operations
2. **Use projected CRS** for area and distance calculations
3. **Match CRS** before spatial joins or overlays
4. **Validate geometries** with `.is_valid` before operations
5. **Use `.copy()`** when modifying geometry columns to avoid side effects
6. **Preserve topology** when simplifying for analysis
7. **Use GeoPackage** format for modern workflows (better than Shapefile)
8. **Set max_distance** in sjoin_nearest for better performance

-e 

---

# GeoPandas Data Structures

## GeoSeries

A GeoSeries is a vector where each entry is a set of shapes corresponding to one observation (similar to a pandas Series but with geometric data).

```python
import geopandas as gpd
from shapely.geometry import Point, Polygon

# Create a GeoSeries from geometries
points = gpd.GeoSeries([Point(1, 1), Point(2, 2), Point(3, 3)])

# Access geometric properties
points.area
points.length
points.bounds
```

## GeoDataFrame

A GeoDataFrame is a tabular data structure that contains a GeoSeries (similar to a pandas DataFrame but with geographic data).

```python
# Create from dictionary
gdf = gpd.GeoDataFrame({
    'name': ['Point A', 'Point B'],
    'value': [100, 200],
    'geometry': [Point(1, 1), Point(2, 2)]
})

# Create from pandas DataFrame with coordinates
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3], 'y': [1, 2, 3], 'name': ['A', 'B', 'C']})
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.x, df.y))
```

## Key Properties

- **geometry**: The active geometry column (can have multiple geometry columns)
- **crs**: Coordinate reference system
- **bounds**: Bounding box of all geometries
- **total_bounds**: Overall bounding box

## Setting Active Geometry

When a GeoDataFrame has multiple geometry columns:

```python
# Set active geometry column
gdf = gdf.set_geometry('other_geom_column')

# Check active geometry column
gdf.geometry.name
```

## Indexing and Selection

Use standard pandas indexing with spatial data:

```python
# Select by label
gdf.loc[0]

# Boolean indexing
large_areas = gdf[gdf.area > 100]

# Select columns
gdf[['name', 'geometry']]
```
-e 

---

# Reading and Writing Spatial Data

## Reading Files

Use `geopandas.read_file()` to import vector spatial data:

```python
import geopandas as gpd

# Read from file
gdf = gpd.read_file("data.shp")
gdf = gpd.read_file("data.geojson")
gdf = gpd.read_file("data.gpkg")

# Read from URL
gdf = gpd.read_file("https://example.com/data.geojson")

# Read from ZIP archive
gdf = gpd.read_file("data.zip")
```

### Performance: Arrow Acceleration

For 2-4x faster reading, use Arrow:

```python
gdf = gpd.read_file("data.gpkg", use_arrow=True)
```

Requires PyArrow: `uv pip install pyarrow`

### Filtering During Read

Pre-filter data to load only what's needed:

```python
# Load specific rows
gdf = gpd.read_file("data.gpkg", rows=100)  # First 100 rows
gdf = gpd.read_file("data.gpkg", rows=slice(10, 20))  # Rows 10-20

# Load specific columns
gdf = gpd.read_file("data.gpkg", columns=['name', 'population'])

# Spatial filter with bounding box
gdf = gpd.read_file("data.gpkg", bbox=(xmin, ymin, xmax, ymax))

# Spatial filter with geometry mask
gdf = gpd.read_file("data.gpkg", mask=polygon_geometry)

# SQL WHERE clause (requires Fiona 1.9+ or Pyogrio)
gdf = gpd.read_file("data.gpkg", where="population > 1000000")

# Skip geometry (returns pandas DataFrame)
df = gpd.read_file("data.gpkg", ignore_geometry=True)
```

## Writing Files

Use `to_file()` to export:

```python
# Write to Shapefile
gdf.to_file("output.shp")

# Write to GeoJSON
gdf.to_file("output.geojson", driver='GeoJSON')

# Write to GeoPackage (supports multiple layers)
gdf.to_file("output.gpkg", layer='layer1', driver="GPKG")

# Arrow acceleration for faster writing
gdf.to_file("output.gpkg", use_arrow=True)
```

### Supported Formats

List all available drivers:

```python
import pyogrio
pyogrio.list_drivers()
```

Common formats: Shapefile, GeoJSON, GeoPackage (GPKG), KML, MapInfo File, CSV (with WKT geometry)

## Parquet and Feather

Columnar formats preserving spatial information with support for multiple geometry columns:

```python
# Write
gdf.to_parquet("data.parquet")
gdf.to_feather("data.feather")

# Read
gdf = gpd.read_parquet("data.parquet")
gdf = gpd.read_feather("data.feather")
```

Advantages:
- Faster I/O than traditional formats
- Better compression
- Preserves multiple geometry columns
- Schema versioning support

## PostGIS Databases

### Reading from PostGIS

```python
from sqlalchemy import create_engine

engine = create_engine('postgresql://user:password@host:port/database')

# Read entire table
gdf = gpd.read_postgis("SELECT * FROM table_name", con=engine, geom_col='geometry')

# Read with SQL query
gdf = gpd.read_postgis("SELECT * FROM table WHERE population > 100000", con=engine, geom_col='geometry')
```

### Writing to PostGIS

```python
# Create or replace table
gdf.to_postgis("table_name", con=engine, if_exists='replace')

# Append to existing table
gdf.to_postgis("table_name", con=engine, if_exists='append')

# Fail if table exists
gdf.to_postgis("table_name", con=engine, if_exists='fail')
```

Requires: `uv pip install psycopg2` or `uv pip install psycopg` and `uv pip install geoalchemy2`

## File-like Objects

Read from file handles or in-memory buffers:

```python
# From file handle
with open('data.geojson', 'r') as f:
    gdf = gpd.read_file(f)

# From StringIO
from io import StringIO
geojson_string = '{"type": "FeatureCollection", ...}'
gdf = gpd.read_file(StringIO(geojson_string))
```

## Remote Storage (fsspec)

Access data from cloud storage:

```python
# S3
gdf = gpd.read_file("s3://bucket/data.gpkg")

# Azure Blob Storage
gdf = gpd.read_file("az://container/data.gpkg")

# HTTP/HTTPS
gdf = gpd.read_file("https://example.com/data.geojson")
```
-e 

---

# Coordinate Reference Systems (CRS)

A coordinate reference system defines how coordinates relate to locations on Earth.

## Understanding CRS

CRS information is stored as `pyproj.CRS` objects:

```python
# Check CRS
print(gdf.crs)

# Check if CRS is set
if gdf.crs is None:
    print("No CRS defined")
```

## Setting vs Reprojecting

### Setting CRS

Use `set_crs()` when coordinates are correct but CRS metadata is missing:

```python
# Set CRS (doesn't transform coordinates)
gdf = gdf.set_crs("EPSG:4326")
gdf = gdf.set_crs(4326)
```

**Warning**: Only use when CRS metadata is missing. This does not transform coordinates.

### Reprojecting

Use `to_crs()` to transform coordinates between coordinate systems:

```python
# Reproject to different CRS
gdf_projected = gdf.to_crs("EPSG:3857")  # Web Mercator
gdf_projected = gdf.to_crs(3857)

# Reproject to match another GeoDataFrame
gdf1_reprojected = gdf1.to_crs(gdf2.crs)
```

## CRS Formats

GeoPandas accepts multiple formats via `pyproj.CRS.from_user_input()`:

```python
# EPSG code (integer)
gdf.to_crs(4326)

# Authority string
gdf.to_crs("EPSG:4326")
gdf.to_crs("ESRI:102003")

# WKT string (Well-Known Text)
gdf.to_crs("GEOGCS[...]")

# PROJ string
gdf.to_crs("+proj=longlat +datum=WGS84")

# pyproj.CRS object
from pyproj import CRS
crs_obj = CRS.from_epsg(4326)
gdf.to_crs(crs_obj)
```

**Best Practice**: Use WKT2 or authority strings (EPSG) to preserve full CRS information.

## Common EPSG Codes

### Geographic Coordinate Systems

```python
# WGS 84 (latitude/longitude)
gdf.to_crs("EPSG:4326")

# NAD83
gdf.to_crs("EPSG:4269")
```

### Projected Coordinate Systems

```python
# Web Mercator (used by web maps)
gdf.to_crs("EPSG:3857")

# UTM zones (example: UTM Zone 33N)
gdf.to_crs("EPSG:32633")

# UTM zones (Southern hemisphere, example: UTM Zone 33S)
gdf.to_crs("EPSG:32733")

# US National Atlas Equal Area
gdf.to_crs("ESRI:102003")

# Albers Equal Area Conic (North America)
gdf.to_crs("EPSG:5070")
```

## CRS Requirements for Operations

### Operations Requiring Matching CRS

These operations require identical CRS:

```python
# Spatial joins
gpd.sjoin(gdf1, gdf2, ...)  # CRS must match

# Overlay operations
gpd.overlay(gdf1, gdf2, ...)  # CRS must match

# Appending
pd.concat([gdf1, gdf2])  # CRS must match

# Reproject first if needed
gdf2_reprojected = gdf2.to_crs(gdf1.crs)
result = gpd.sjoin(gdf1, gdf2_reprojected)
```

### Operations Best in Projected CRS

Area and distance calculations should use projected CRS:

```python
# Bad: area in degrees (meaningless)
areas_degrees = gdf.geometry.area  # If CRS is EPSG:4326

# Good: reproject to appropriate projected CRS first
gdf_projected = gdf.to_crs("EPSG:3857")
areas_meters = gdf_projected.geometry.area  # Square meters

# Better: use appropriate local UTM zone for accuracy
gdf_utm = gdf.to_crs("EPSG:32633")  # UTM Zone 33N
accurate_areas = gdf_utm.geometry.area
```

## Choosing Appropriate CRS

### For Area/Distance Calculations

Use equal-area projections:

```python
# Albers Equal Area Conic (North America)
gdf.to_crs("EPSG:5070")

# Lambert Azimuthal Equal Area
gdf.to_crs("EPSG:3035")  # Europe

# UTM zones (for local areas)
gdf.to_crs("EPSG:32633")  # Appropriate UTM zone
```

### For Distance-Preserving (Navigation)

Use equidistant projections:

```python
# Azimuthal Equidistant
gdf.to_crs("ESRI:54032")
```

### For Shape-Preserving (Angles)

Use conformal projections:

```python
# Web Mercator (conformal but distorts area)
gdf.to_crs("EPSG:3857")

# UTM zones (conformal for local areas)
gdf.to_crs("EPSG:32633")
```

### For Web Mapping

```python
# Web Mercator (standard for web maps)
gdf.to_crs("EPSG:3857")
```

## Estimating UTM Zone

```python
# Estimate appropriate UTM CRS from data
utm_crs = gdf.estimate_utm_crs()
gdf_utm = gdf.to_crs(utm_crs)
```

## Multiple Geometry Columns with Different CRS

GeoPandas 0.8+ supports different CRS per geometry column:

```python
# Set CRS for specific geometry column
gdf = gdf.set_crs("EPSG:4326", allow_override=True)

# Active geometry determines operations
gdf = gdf.set_geometry('other_geom_column')

# Check CRS mismatch
try:
    result = gdf1.overlay(gdf2)
except ValueError as e:
    print("CRS mismatch:", e)
```

## CRS Information

```python
# Get full CRS details
print(gdf.crs)

# Get EPSG code if available
print(gdf.crs.to_epsg())

# Get WKT representation
print(gdf.crs.to_wkt())

# Get PROJ string
print(gdf.crs.to_proj4())

# Check if CRS is geographic (lat/lon)
print(gdf.crs.is_geographic)

# Check if CRS is projected
print(gdf.crs.is_projected)
```

## Transforming Individual Geometries

```python
from pyproj import Transformer

# Create transformer
transformer = Transformer.from_crs("EPSG:4326", "EPSG:3857", always_xy=True)

# Transform point
x_new, y_new = transformer.transform(x, y)
```
-e 

---

# Geometric Operations

GeoPandas provides extensive geometric manipulation through Shapely integration.

## Constructive Operations

Create new geometries from existing ones:

### Buffer

Create geometries representing all points within a distance:

```python
# Buffer by fixed distance
buffered = gdf.geometry.buffer(10)

# Negative buffer (erosion)
eroded = gdf.geometry.buffer(-5)

# Buffer with resolution parameter
smooth_buffer = gdf.geometry.buffer(10, resolution=16)
```

### Boundary

Get lower-dimensional boundary:

```python
# Polygon -> LineString, LineString -> MultiPoint
boundaries = gdf.geometry.boundary
```

### Centroid

Get center point of each geometry:

```python
centroids = gdf.geometry.centroid
```

### Convex Hull

Smallest convex polygon containing all points:

```python
hulls = gdf.geometry.convex_hull
```

### Concave Hull

Smallest concave polygon containing all points:

```python
# ratio parameter controls concavity (0 = convex hull, 1 = most concave)
concave_hulls = gdf.geometry.concave_hull(ratio=0.5)
```

### Envelope

Smallest axis-aligned rectangle:

```python
envelopes = gdf.geometry.envelope
```

### Simplify

Reduce geometric complexity:

```python
# Douglas-Peucker algorithm with tolerance
simplified = gdf.geometry.simplify(tolerance=10)

# Preserve topology (prevents self-intersections)
simplified = gdf.geometry.simplify(tolerance=10, preserve_topology=True)
```

### Segmentize

Add vertices to line segments:

```python
# Add vertices with maximum segment length
segmented = gdf.geometry.segmentize(max_segment_length=5)
```

### Union All

Combine all geometries into single geometry:

```python
# Union all features
unified = gdf.geometry.union_all()
```

## Affine Transformations

Mathematical transformations of coordinates:

### Rotate

```python
# Rotate around origin (0, 0) by angle in degrees
rotated = gdf.geometry.rotate(angle=45, origin='center')

# Rotate around custom point
rotated = gdf.geometry.rotate(angle=45, origin=(100, 100))
```

### Scale

```python
# Scale uniformly
scaled = gdf.geometry.scale(xfact=2.0, yfact=2.0)

# Scale with origin
scaled = gdf.geometry.scale(xfact=2.0, yfact=2.0, origin='center')
```

### Translate

```python
# Shift coordinates
translated = gdf.geometry.translate(xoff=100, yoff=50)
```

### Skew

```python
# Shear transformation
skewed = gdf.geometry.skew(xs=15, ys=0, origin='center')
```

### Custom Affine Transform

```python
from shapely import affinity

# Apply 6-parameter affine transformation matrix
# [a, b, d, e, xoff, yoff]
transformed = gdf.geometry.affine_transform([1, 0, 0, 1, 100, 50])
```

## Geometric Properties

Access geometric properties (returns pandas Series):

```python
# Area
areas = gdf.geometry.area

# Length/perimeter
lengths = gdf.geometry.length

# Bounding box coordinates
bounds = gdf.geometry.bounds  # Returns DataFrame with minx, miny, maxx, maxy

# Total bounds for entire GeoSeries
total_bounds = gdf.geometry.total_bounds  # Returns array [minx, miny, maxx, maxy]

# Check geometry types
geom_types = gdf.geometry.geom_type

# Check if valid
is_valid = gdf.geometry.is_valid

# Check if empty
is_empty = gdf.geometry.is_empty
```

## Geometric Relationships

Binary predicates testing relationships:

```python
# Within
gdf1.geometry.within(gdf2.geometry)

# Contains
gdf1.geometry.contains(gdf2.geometry)

# Intersects
gdf1.geometry.intersects(gdf2.geometry)

# Touches
gdf1.geometry.touches(gdf2.geometry)

# Crosses
gdf1.geometry.crosses(gdf2.geometry)

# Overlaps
gdf1.geometry.overlaps(gdf2.geometry)

# Covers
gdf1.geometry.covers(gdf2.geometry)

# Covered by
gdf1.geometry.covered_by(gdf2.geometry)
```

## Point Extraction

Extract specific points from geometries:

```python
# Representative point (guaranteed to be within geometry)
rep_points = gdf.geometry.representative_point()

# Interpolate point along line at distance
points = line_gdf.geometry.interpolate(distance=10)

# Interpolate point at normalized distance (0 to 1)
midpoints = line_gdf.geometry.interpolate(distance=0.5, normalized=True)
```

## Delaunay Triangulation

```python
# Create triangulation
triangles = gdf.geometry.delaunay_triangles()
```
-e 

---

# Spatial Analysis

## Attribute Joins

Combine datasets based on common variables using standard pandas merge:

```python
# Merge on common column
result = gdf.merge(df, on='common_column')

# Left join
result = gdf.merge(df, on='common_column', how='left')

# Important: Call merge on GeoDataFrame to preserve geometry
# This works: gdf.merge(df, ...)
# This doesn't: df.merge(gdf, ...) # Returns DataFrame, not GeoDataFrame
```

## Spatial Joins

Combine datasets based on spatial relationships.

### Binary Predicate Joins (sjoin)

Join based on geometric predicates:

```python
# Intersects (default)
joined = gpd.sjoin(gdf1, gdf2, how='inner', predicate='intersects')

# Available predicates
joined = gpd.sjoin(gdf1, gdf2, predicate='contains')
joined = gpd.sjoin(gdf1, gdf2, predicate='within')
joined = gpd.sjoin(gdf1, gdf2, predicate='touches')
joined = gpd.sjoin(gdf1, gdf2, predicate='crosses')
joined = gpd.sjoin(gdf1, gdf2, predicate='overlaps')

# Join types
joined = gpd.sjoin(gdf1, gdf2, how='left')   # Keep all from left
joined = gpd.sjoin(gdf1, gdf2, how='right')  # Keep all from right
joined = gpd.sjoin(gdf1, gdf2, how='inner')  # Intersection only
```

The `how` parameter determines which geometries are retained:
- **left**: Retains left GeoDataFrame's index and geometry
- **right**: Retains right GeoDataFrame's index and geometry
- **inner**: Uses intersection of indices, keeps left geometry

### Nearest Joins (sjoin_nearest)

Join to nearest features:

```python
# Find nearest neighbor
nearest = gpd.sjoin_nearest(gdf1, gdf2)

# Add distance column
nearest = gpd.sjoin_nearest(gdf1, gdf2, distance_col='distance')

# Limit search radius (significantly improves performance)
nearest = gpd.sjoin_nearest(gdf1, gdf2, max_distance=1000)

# Find k nearest neighbors
nearest = gpd.sjoin_nearest(gdf1, gdf2, k=5)
```

## Overlay Operations

Set-theoretic operations combining geometries from two GeoDataFrames:

```python
# Intersection - keep areas where both overlap
intersection = gpd.overlay(gdf1, gdf2, how='intersection')

# Union - combine all areas
union = gpd.overlay(gdf1, gdf2, how='union')

# Difference - areas in first not in second
difference = gpd.overlay(gdf1, gdf2, how='difference')

# Symmetric difference - areas in either but not both
sym_diff = gpd.overlay(gdf1, gdf2, how='symmetric_difference')

# Identity - intersection + difference
identity = gpd.overlay(gdf1, gdf2, how='identity')
```

Result includes attributes from both input GeoDataFrames.

## Dissolve (Aggregation)

Aggregate geometries based on attribute values:

```python
# Dissolve by attribute
dissolved = gdf.dissolve(by='region')

# Dissolve with aggregation functions
dissolved = gdf.dissolve(by='region', aggfunc='sum')
dissolved = gdf.dissolve(by='region', aggfunc={'population': 'sum', 'area': 'mean'})

# Dissolve all into single geometry
dissolved = gdf.dissolve()

# Preserve internal boundaries
dissolved = gdf.dissolve(by='region', as_index=False)
```

## Clipping

Clip geometries to boundary of another geometry:

```python
# Clip to polygon boundary
clipped = gpd.clip(gdf, boundary_polygon)

# Clip to another GeoDataFrame
clipped = gpd.clip(gdf, boundary_gdf)
```

## Appending

Combine multiple GeoDataFrames:

```python
import pandas as pd

# Concatenate GeoDataFrames (CRS must match)
combined = pd.concat([gdf1, gdf2], ignore_index=True)

# With keys for identification
combined = pd.concat([gdf1, gdf2], keys=['source1', 'source2'])
```

## Spatial Indexing

Improve performance for spatial operations:

```python
# GeoPandas uses spatial index automatically for most operations
# Access the spatial index directly
sindex = gdf.sindex

# Query geometries intersecting a bounding box
possible_matches_index = list(sindex.intersection((xmin, ymin, xmax, ymax)))
possible_matches = gdf.iloc[possible_matches_index]

# Query geometries intersecting a polygon
possible_matches_index = list(sindex.query(polygon_geometry))
possible_matches = gdf.iloc[possible_matches_index]
```

Spatial indexing significantly speeds up:
- Spatial joins
- Overlay operations
- Queries with geometric predicates

## Distance Calculations

```python
# Distance between geometries
distances = gdf1.geometry.distance(gdf2.geometry)

# Distance to single geometry
distances = gdf.geometry.distance(single_point)

# Minimum distance to any feature
min_dist = gdf.geometry.distance(point).min()
```

## Area and Length Calculations

For accurate measurements, ensure proper CRS:

```python
# Reproject to appropriate projected CRS for area/length calculations
gdf_projected = gdf.to_crs(epsg=3857)  # Or appropriate UTM zone

# Calculate area (in CRS units, typically square meters)
areas = gdf_projected.geometry.area

# Calculate length/perimeter (in CRS units)
lengths = gdf_projected.geometry.length
```
-e 

---

# Mapping and Visualization

GeoPandas provides plotting through matplotlib integration.

## Basic Plotting

```python
# Simple plot
gdf.plot()

# Customize figure size
gdf.plot(figsize=(10, 10))

# Set colors
gdf.plot(color='blue', edgecolor='black')

# Control line width
gdf.plot(edgecolor='black', linewidth=0.5)
```

## Choropleth Maps

Color features based on data values:

```python
# Basic choropleth
gdf.plot(column='population', legend=True)

# Specify colormap
gdf.plot(column='population', cmap='OrRd', legend=True)

# Other colormaps: 'viridis', 'plasma', 'inferno', 'YlOrRd', 'Blues', 'Greens'
```

### Classification Schemes

Requires: `uv pip install mapclassify`

```python
# Quantiles
gdf.plot(column='population', scheme='quantiles', k=5, legend=True)

# Equal interval
gdf.plot(column='population', scheme='equal_interval', k=5, legend=True)

# Natural breaks (Fisher-Jenks)
gdf.plot(column='population', scheme='fisher_jenks', k=5, legend=True)

# Other schemes: 'box_plot', 'headtail_breaks', 'max_breaks', 'std_mean'

# Pass parameters to classification
gdf.plot(column='population', scheme='quantiles', k=7,
         classification_kwds={'pct': [10, 20, 30, 40, 50, 60, 70, 80, 90]})
```

### Legend Customization

```python
# Position legend outside plot
gdf.plot(column='population', legend=True,
         legend_kwds={'loc': 'upper left', 'bbox_to_anchor': (1, 1)})

# Horizontal legend
gdf.plot(column='population', legend=True,
         legend_kwds={'orientation': 'horizontal'})

# Custom legend label
gdf.plot(column='population', legend=True,
         legend_kwds={'label': 'Population Count'})

# Use separate axes for colorbar
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1, figsize=(10, 6))
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)
gdf.plot(column='population', ax=ax, legend=True, cax=cax)
```

## Handling Missing Data

```python
# Style missing values
gdf.plot(column='population',
         missing_kwds={'color': 'lightgrey', 'edgecolor': 'red', 'hatch': '///',
                      'label': 'Missing data'})
```

## Multi-Layer Maps

Combine multiple GeoDataFrames:

```python
import matplotlib.pyplot as plt

# Create base plot
fig, ax = plt.subplots(figsize=(10, 10))

# Add layers
gdf1.plot(ax=ax, color='lightblue', edgecolor='black')
gdf2.plot(ax=ax, color='red', markersize=5)
gdf3.plot(ax=ax, color='green', alpha=0.5)

plt.show()

# Control layer order with zorder (higher = on top)
gdf1.plot(ax=ax, zorder=1)
gdf2.plot(ax=ax, zorder=2)
```

## Styling Options

```python
# Transparency
gdf.plot(alpha=0.5)

# Marker style for points
points.plot(marker='o', markersize=50)
points.plot(marker='^', markersize=100, color='red')

# Line styles
lines.plot(linestyle='--', linewidth=2)
lines.plot(linestyle=':', color='blue')

# Categorical coloring
gdf.plot(column='category', categorical=True, legend=True)

# Vary marker size by column
gdf.plot(markersize=gdf['value']/1000)
```

## Map Enhancements

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 8))
gdf.plot(ax=ax, column='population', legend=True)

# Add title
ax.set_title('Population by Region', fontsize=16)

# Add axis labels
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# Remove axes
ax.set_axis_off()

# Add north arrow and scale bar (requires separate packages)
# See geopandas-plot or contextily for these features

plt.tight_layout()
plt.show()
```

## Interactive Maps

Requires: `uv pip install folium`

```python
# Create interactive map
m = gdf.explore(column='population', cmap='YlOrRd', legend=True)
m.save('map.html')

# Customize base map
m = gdf.explore(tiles='OpenStreetMap', legend=True)
m = gdf.explore(tiles='CartoDB positron', legend=True)

# Add tooltip
m = gdf.explore(column='population', tooltip=['name', 'population'], legend=True)

# Style options
m = gdf.explore(color='red', style_kwds={'fillOpacity': 0.5, 'weight': 2})

# Multiple layers
m = gdf1.explore(color='blue', name='Layer 1')
gdf2.explore(m=m, color='red', name='Layer 2')
folium.LayerControl().add_to(m)
```

## Integration with Other Plot Types

GeoPandas supports pandas plot types:

```python
# Histogram of attribute
gdf['population'].plot.hist(bins=20)

# Scatter plot
gdf.plot.scatter(x='income', y='population')

# Box plot
gdf.boxplot(column='population', by='region')
```

## Basemaps with Contextily

Requires: `uv pip install contextily`

```python
import contextily as ctx

# Reproject to Web Mercator for basemap compatibility
gdf_webmercator = gdf.to_crs(epsg=3857)

fig, ax = plt.subplots(figsize=(10, 10))
gdf_webmercator.plot(ax=ax, alpha=0.5, edgecolor='k')

# Add basemap
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
# Other sources: ctx.providers.CartoDB.Positron, ctx.providers.Stamen.Terrain

plt.show()
```

## Cartographic Projections with CartoPy

Requires: `uv pip install cartopy`

```python
import cartopy.crs as ccrs

# Create map with specific projection
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.Robinson()}, figsize=(15, 10))

gdf.plot(ax=ax, transform=ccrs.PlateCarree(), column='population', legend=True)

ax.coastlines()
ax.gridlines(draw_labels=True)

plt.show()
```

## Saving Figures

```python
# Save to file
ax = gdf.plot()
fig = ax.get_figure()
fig.savefig('map.png', dpi=300, bbox_inches='tight')
fig.savefig('map.pdf')
fig.savefig('map.svg')
```
