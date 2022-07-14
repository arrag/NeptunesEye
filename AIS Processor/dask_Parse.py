# dask Parser - WIP 
# after downloading the Zip - 

import requests
import shutil
from csv import reader

from downloader import AISfile
import dask.dataframe as dd

data1 =  AISfile

def LocationParse():

    df = dd.read_csv(data1) # location is the Houston / Galveston Area 
    df = df[(df['LAT'] >=29.190) & (df['LAT'] <=29.860 )]
    df = df[(df['LON'] >=-95.080) & (df['LON'] <=-94.490)]
    df = df.compute
    