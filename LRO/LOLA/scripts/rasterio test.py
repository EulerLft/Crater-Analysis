#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:14:44 2026

@author: eulerlft
"""

from pathlib import Path
import rasterio

lola_root = Path(__file__).resolve().parent.parent

DATA_PATH = lola_root / 'data/gdr_cylindrical'

lbl_path = DATA_PATH / "ldec_1024_00n_15n_000_030.lbl"

with rasterio.open(lbl_path) as src:
  print("Raster width: ", src.width)
  print("Raster height: ", src.height)
  print("Coordinate Reference System: ", src.crs)
  print("Bounds: ", src.bounds)