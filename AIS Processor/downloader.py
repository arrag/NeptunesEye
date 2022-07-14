# script to pull ais feed from NOAA feed
# https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2022/index.html 
# feed found above 
# parse each file for a given vessel type - or a list of vessels to create a //
# historical track? could pick specific vessels or flags // IE russia 
# or could pic geographic regions to focus on -- 
#
# Reqs / pandas 
#

import datetime as timer
import requests
import shutil
import pandas as pd
import zipfile
from dask_Parse import LocationParse




def download_data(AISfile):
    url='http://coast.noaa.gov/htdata/CMSP/AISDataHandler/2022/'+AISfile+'.ZIP'   

    zip_filename=AISfile+'.zip'
    try:#https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2022/AIS_2022_01_01.zip
        print('Calling url:- ' + url)
        r = requests.get(url, stream=True,verify=False)
        if r.status_code == 200:
            with open(zip_filename, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        r.close()
    except Exception as e:
        print('for Date '+ AISfile +' Exception happened, EXCEPTION Message is ' + str(e))


def AISpull():
    i=0
     # now = str('2022')+str('_')+str('04')+str('_')+str('01')   #  now = timer.datetime.now()  - loop worked from today but files are only updated through March
    day = 1  #day = now.day (First)
    month = 4   #month = now.month (April)
    year = 2022     #year = now.year
    while i<10: #sets how many days you want to pull from your start date
        day=day-1
        if day==0:
            day=31
            month=month-1
            if month==0:
                month=12
                year=year-1
        year1=year
        month1='{:02d}'.format(month)
        day1='{:02d}'.format(day)
        AISfile=str('AIS_')+str(year1)+str('_')+str(month1)+str('_')+str(day1)
        download_data(AISfile)
        i+=1
        result = None 
        
        # need to unzip file - then run the parse 

        LocationParse() 


if __name__=='__main__':
    AISpull()


# File is now downloaded and stored locally 
# need to open in chunks and parse 
# filter for key parameters


#  zf = zipfile.ZipFile('')

# MMSI	BaseDateTime	LAT	LON	SOG	COG	Heading	VesselName	IMO	CallSign	VesselType	Status	Length	Width	Draft	Cargo	TransceiverClass

