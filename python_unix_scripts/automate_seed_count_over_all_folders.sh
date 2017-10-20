#!/bin/bash

#This script runs the python script I wrote to count seeds
#Because I did not add this script to the ENV path it can only be run from within the folder it is located. 
#The results of the seed counts goes to the output folder in the Decodon project folder, although the use can define for themselves where to store the output by changing the path specified here. 

for folder in /Users/Maggie/Documents/Decodon/Seed_counting/Seed_photos/*201*/ ; 
	do python /Users/Maggie/Documents/Decodon/Decodon_2015/python_unix_scripts/Decodon_seed_counts_circle_correction2.py $folder  >> /Users/Maggie/Documents/Decodon/Decodon_2015/output/seed_count_June8_night_2016.txt  2> bad_photos.txt; 
done

