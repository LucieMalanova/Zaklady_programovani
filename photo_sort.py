#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[7]:


from PIL import Image
from PIL.ExifTags import TAGS
import os
import shutil
import argparse
import gmaps
from ipywidgets.embed import embed_minimal_html
import sys


# In[9]:


#create dictionary(tag:decoded data) of exif data for one photo
#input: exifdata
#output: exif_dict

def get_exif_dict(exifdata):
    tags = []
    data = []

    #extract tags and data from the exif data file and append them to lists
    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        value = exifdata.get(tag_id)

        tags.append(tag)
        data.append(value)

    #create dictionary out of lists
    zip_exif = zip(tags,data)
    exif_dict = dict(zip_exif)
    
    return exif_dict, tags

#get coordinates from exif data
#input: exif_dict[gps_tag]
#output: coordinates - tuple(latitude,longitude)

def get_coords(gps_tag, exif_dict):
    
    lat_sign = exif_dict[gps_tag][1]
    if lat_sign == 'N':
        lat_sign = 1
    if lat_sign == 'S':
        lat_sign = -1
    lat_converted = exif_dict[gps_tag][2][0]
    lat_converted += exif_dict[gps_tag][2][1] / 60
    lat_converted += exif_dict[gps_tag][2][2] / 3600
    latitude = lat_sign * float(lat_converted)

    long_sign = exif_dict[gps_tag][3]
    if long_sign == 'E':
        long_sign = 1
    if long_sign == 'W':
        long_sign = -1
    long_converted = exif_dict[gps_tag][4][0]
    long_converted += exif_dict[gps_tag][4][1] / 60
    long_converted += exif_dict[gps_tag][4][2] / 3600
    longitude = long_sign * float(long_converted)

    coordinates = (latitude, longitude)
    return coordinates

#get new name based on date
#input: exif data, photo path, list to append new names to
#output: new_name

def get_new_name(date_tag, tags, exif_dict, original_photo, new_names):
    if date_tag in tags:
        raw_date = exif_dict[date_tag][0:10]
        date = raw_date.replace(':','-') + '_'
    else:
        date = ''

    separator = original_photo[::-1].find('.')
    photo_format = original_photo[-separator-1:].lower()
    counter = 1
    new_name = date + str(counter).zfill(3) + photo_format
    
    while new_name in new_names:
        counter += 1
        new_name = date + str(counter).zfill(3) + photo_format
        
    return new_name

#create a copy directory including the files
#input: output_folder, input_folder
#output: none

def copy_all_files(output_folder, input_folder):
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)   
    shutil.copytree(input_folder,output_folder,
                    symlinks=False, ignore=None,
                    dirs_exist_ok=True)

    
#rename photos in output folder according to new names
#input: list of old file names, list of new file names and output folder path
#output: none

def rename_files(old_names, new_names, output_folder):
    number_files = len(old_names)
    for i in range(number_files):
        old_copy_src = os.path.join(output_folder, old_names[i])
        new_copy_dst = os.path.join(output_folder, new_names[i])
        os.rename(old_copy_src, new_copy_dst)

        year = new_names[i][:4]
        if "." in year:
            year = 'unknown'

        year_folder = os.path.join(output_folder,year)
        if not os.path.exists(year_folder):
            os.mkdir(year_folder)

        new_sort_dst = os.path.join(year_folder, new_names[i])
        shutil.move(new_copy_dst, new_sort_dst)
        
#process optional arguments from terminal
#input: coordinates_list, output_folder, input_folder
#output: none

def process_opt_args(args, coordinates_list, output_folder, input_folder):
    

    if args.m:
        gmaps.configure(api_key='AIzaSyDnKEkX7BgefnKMaCYHCLES7yed_Ff4yAM')
        fig = gmaps.figure()
        markers = gmaps.marker_layer(coordinates_list)
        fig.add_layer(markers)
        map_path = os.path.join(output_folder,'photosort_map.html')
        embed_minimal_html(map_path, views=[fig], title='photo_map')
        print('The map is generated in the output folder.')
    
    if args.x:
        confirm = input('Do you really want to delete the input dir with original photos? [y/n]')
        if confirm.lower() != 'y':
            print('not deleting original photos')
        else:
            print('deleting the input folder with original photos.')
            shutil.rmtree(input_folder)


# In[4]:


#check inputs, count number of files in input folder

parser = argparse.ArgumentParser()
parser.add_argument("-m", action = 'store_true', help='show photos on map')
parser.add_argument("-x", action = 'store_true',
                    help='delete photos from input folder')
args, paths = parser.parse_known_args()

number_args = len(paths)
if number_args < 1:
    print("You have to enter at least the input directory.")
    print("Enter the input dir and run the script again.")
    sys.exit()

input_folder = str(paths[0])

if not os.path.exists(input_folder):
    print("Your input directory doesn't exist")
    print("Check the input path and run the script again.")
    sys.exit()
    
if number_args < 2:
    parent_folder = os.path.abspath(os.path.join(input_folder, os.pardir))
    output_folder = os.path.join(parent_folder, 'output_folder')
    print("You haven't specified your output directory. New output directory will be created here:")
    print(output_folder)
    confirm = input('Do you want to continue with this folder? If no,' +
              'run the script again and enter output folder. [y/n]')
    if confirm.lower() != 'y':
        print('Ending the program.')
        sys.exit()
    else:
        print('Creating new directory.')
    
    
if number_args == 2:
    output_folder = str(paths[1])


photos_list = os.listdir(input_folder) 
number_files = len(photos_list)


#access the images from input_folder
old_names = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]   


#access exif data from a photo
new_names = []
coordinates_list = []

for i in range(number_files):
    
    original_photo = os.path.join(input_folder, old_names[i])
    
    with Image.open(original_photo)as image:
        exifdata = image.getexif()

    #create dictionary of exif data for one photo
    exif_dict,tags = get_exif_dict(exifdata)
    
    #get gps data
    gps_tag = 'GPSInfo'
    
    if gps_tag in tags:
        coordinates = get_coords(gps_tag, exif_dict)
        coordinates_list.append(coordinates)  
    
    #find date and format new name
    
    date_tag = "DateTimeOriginal"
    
    new_name = get_new_name(date_tag, tags, exif_dict,
                            original_photo, new_names)
    
    new_names.append(new_name)

#copy the files to output folder    
copy_all_files(output_folder,input_folder)
print('All photos are copied.')

#rename photos in output folder
rename_files(old_names, new_names, output_folder)
print('All photos are renamed.')

#process optional arguments (create maps, delete photos)
process_opt_args(args, coordinates_list, output_folder, input_folder)

print('Done.')

