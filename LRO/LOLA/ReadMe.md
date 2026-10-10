# LRO - Lunar Reconnaissance Orbiter 

---

## Description 

NASA's LRO (Lunar Reconnaissance Orbiter) has been studyign the Moon since 2009 - longest lived lunar orbiting mission. <br>
It has mapped the Moon's surface and measured temperature, composition and radiation environment in unprecedented detail. Data from LRO enables us to select locations on the lunar surface where spacecrafts may safely land. <br> 

It enables the analysis of the Moon's South Pole with crucial resources like water and extended sunlight which provides power for equipment and supports exploration activities.  <br> 

Type: orbiter  <br> 
Target: Earth's Moon <br> 
Launch: June 18, 2009 <br> 


LRO has already collected as much data as all other planetary missions combined. <br>
This volume of data is possible because the Moon is so close to Earth and because LRO has its own dedicated ground station, which means it doesn't have to share time on the Deep Space Network. <br> 
LRO has surpassed its original science goals and is now paving the way for Artemis. <br> 

## Topographic Maps 

Topographic maps of the Moon based on data from LRO's Lunar Orbiter Laser Altimeter (LOLA) instrument are the most accurate to date. <br> 
The final set of data from the exploration phase of the LRO mission was released to the NASA Planetary Data System. <br> 


## Anaglyph 

Stereoscopic 3D effect achieved by encoding slightly offset images using filters of different (chromatically opposite) colours. <br> 
The Narrow Angle Camera (NAC) team generates anaglyphs from pairs of stereo images. <br> 

## Mapping Mineralogy Across the Moon 

The Moon's crust is made up of anorthsite (plagioclase feldspar) and basalt. 


# Lunar Orbiter Laser Altimeter (LOLA)

LOLA PDS Repository: [https://pds-geosciences.wustl.edu/lro/lro-l-lola-3-rdr-v1/lrolol_1xxx/](URL)

<b>Archive Overview<b>: <br> 
Archive contains instrument altimetry data from NASA's LOLA instrument. <br>

<b>Volume Structure<b>: <br>
Higher-level reduced data products are housed on volume `LROLOL_1XXX` which is the primary source for gridded products. 

## Project Structure
```
/home/eulerlft/Project/planetary_research/Crater Analysis/LRO/LOLA/
├── data/
│   └── gdr_cylindrical/     # Local destination for downloaded .img and .lbl files
└── scripts/
    ├── test1.py             # Validates rasterio metadata reading and CRS on sample tiles
    └── pull_pds_repository.py # Automated scraper using requests, BeautifulSoup, and urljoin
```

### Key Directories: 
- `DATA/LOLA_GDR`: Contains Gridded Data Records including topography, slope, counts and roughness data. 
- `DOCUMENT`: Contains Software Interface Specifications (SIS) detailing file structures and formats. 
- `CATALOG`: Houses dataset descriptions and instrtument documentation (`INST.CAT`, `GDR_DS.CAT`). 

### File Conventions: 
All datafiles are accompanied by detached PDS label files sharing the same name with a `.LBL` extension. 

## GDR Cylindrical Datasets 

The Gridded Data Records (GDR) cylindrical dataset contains processed raster products projected onto a regular latitude-longitude grid using a simple cylindrical (equirectagular) map projection optimized for the Moon (`SIMPLE_CYLINDRICAL MOON`). <br> 

Each spatial tile splits global or regional lunar topography into manageable dimensions, mapping elevation, radius, or derived morphologic properties into structured arrays readable by geospatial tools like `Rasterio`. 

## Automation Scripts
- `test1.py`: Connects via pathlib to the local data directory, opens local `.lbl` files using `Rasterio`, and verifies raster dimensions, coordinate reference systems, and spatial bounding boxes. 

- `pull_pds_repository.py`: Scrapes the PDS server directory listing, parses tile links matching `img` and `.lbl` extensions, resolves absolute paths using `urljoin`, and streams files directly into the local data directory while avoiding duplicate downloads.

## Environment Setup

To run the pipeline and scripts, activate the dedicated conda environment and ensure the required geospatial and utility packages are installed:

```
conda activate crater_analysis
```

Required Packages:

`rasterio` (Geospatial raster analysis)
`requests` (HTTP requests for web scraping and downloading)
`beautifulsoup4` (HTML parsing for PDS directory directories)
`pathlib` (Environment-agnostic path management, part of Python standard library)

## Usage Guide

Execute the scraper script from the terminal inside the `scripts/` directory to automatically harvest `.img` and `.lbl` tiles from the PDS server:

```
python pull_pds_repository.py
```

Run the validation script to test reading metadata and spatial properties from downloaded tiles:

```
python test1.py
```


