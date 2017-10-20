Scripts:


PYTHON:
1. Decodon_seed_counts_circle_correction2.py : this script pulls in photos of seeds, converts them into binary images and then removes objects that are not circles and that do not pass a size filter. This is the best script for counting seeds. It corrects for the shape of objects. It removes anything that is not a good circle. 

2.”merge_photos_to_seed_envelopes.py” I started writing this, but I used R to do the data merging of the seed counts done by hand with that done with image analysis. There are 256 fruits (out of 2499 fruits in total) which were counted using image analysis. the difference between the two techniques is small so this was not changed. 

UNIX:
1. "scripts for file and directory manipulation.txt" : this script takes a folder of files and then sorts them into new folders based on their creation date. For example, this script can take a folder of photos off a camera and then sort them into folders by date.
 
2. "automate_seed_count_over_all_folders.sh" : this script is an shell script that automates running the python script for seed counting to run across all folders that have photos. 
