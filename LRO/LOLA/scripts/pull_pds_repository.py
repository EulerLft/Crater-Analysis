#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:34:31 2026

@author: eulerlft
"""

from pathlib import Path 
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup 

# ====================================
# DATA DIRECTORY PATH 
# ====================================

lola_root = Path(__file__).resolve().parent.parent
data_path = lola_root / 'data' / 'gdr_cylindrical'
data_path.mkdir(parents=True, exist_ok=True)

# -----------------------------------
# Change url as necessary 
# -----------------------------------

url = "https://pds-geosciences.wustl.edu/lro/lro-l-lola-3-rdr-v1/lrolol_1xxx/data/lola_gdr/cylindrical/img/"



response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a'):
    href = link.get('href')
    if href and (href.endswith('.img') or href.endswith('.lbl')):
        file_url = urljoin(url, href)
        file_path = data_path / Path(href).name
        
        if not file_path.exists():
            print(f'Downloading {Path(href).name}')
            file_response = requests.get(file_url, stream=True)
            file_response.raise_for_status()
            with open(file_path, 'wb') as f:
                for chunk in file_response.iter_content(chunk_size=8192):
                    f.write(chunk)
        else:
            print(f'Skipping {Path(href).name}, already exists.')