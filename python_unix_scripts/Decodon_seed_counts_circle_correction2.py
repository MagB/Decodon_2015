#!/usr/bin/env python
# -*- coding: utf-8 -*-

# April 18 I started using a differnt lighting for the seeds, so will have to adjust the seed size filter for pics before this date and those after this date.


#SEED COUNTING SCRIPT, OPTIMIZED FOR DECODON 

# Here, I adapt a script from http://scikit-image.org/docs/dev/auto_examples/plot_regional_maxima.html which uses morphological reconstruction to create a background image, which is then subtracted from the original image to isolate bright features (regional maxima).

#Citation:
#Copyright (C) 2011, the scikit-image team
#http://scikit-image.org/
#https://peerj.com/articles/453/
# First we try reconstruction by dilation starting at the edges of the image. We
# initialize a seed image to the minimum intensity of the image, and set its
# border to be the pixel values in the original image. These maximal pixels will
# get dilated in order to reconstruct the background image.

#scikit-image: Image processing in Python.
import numpy as np
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt
#from math import pi

from skimage import data
from skimage import img_as_float
from skimage.morphology import reconstruction
import cv2
from skimage import feature
import pylab
from skimage import *
from skimage.filter import threshold_otsu 
from skimage.filter import threshold_isodata 
from skimage import filter
from skimage import measure
from skimage import io
import skimage.morphology, skimage.data
import os,time,sys
import matplotlib.image as mpimg
 
#set directory with the photos

#dir_input = sys.argv[1]
dir_input = '/Users/Maggie/Documents/Decodon/Seed_counting/Seed_photos/April_18_2016/'

#dir_output = sys.argv[2]
#print dir_input, dir_output
dir_output = '/Users/Maggie/Documents/Decodon/Seed_counting/Counted_photos/'

#loop over the list of photos in that directory
#note that os.listdir is a function in python that makes a list of all the files in a folder

#output is date_of_photo Photo_ID Seed_count area_of_objects_counted

#print ",".join(["Date_taken", "Photo_ID","Seed_count"])


for photo in os.listdir(dir_input):
   # photo="IMG_8140.JPG"
    if not photo.endswith(".JPG"):
        continue
    #photo="IMG_8120.JPG"
    #print dir_input+str(i)+'.JPG'
    
    im =  cv2.imread(dir_input+str(photo),0)
    
#    th3 = cv2.adaptiveThreshold(im,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

    # Convert to float: Important for subtraction later which won't work with uint8
    
    image = img_as_float(im)
    image = gaussian_filter(image, 2)
    #im = ndi.gaussian_filter(image, 4)


    
    seed = np.copy(image)
    seed[1:-1, 1:-1] = image.min()
    mask = image
    
    dilated = reconstruction(seed, mask, method='dilation')
    

    
   # plt.imshow(dilated)
 #   plt.show()
    
    
    
    #FOR EACH UNIQUE IMAGE SET YOU NEED TO FIND THE RIGHT h VALUE 
    
   # h = 0.4
    h = 0.2
    seed = image - h
    dilated = reconstruction(seed, mask, method='dilation')
    hdome = image - dilated
    
 
    
    thresh = threshold_otsu(dilated)
    
   # thresh = threshold_isodata(dilated)
    
    #thresh = threshold_li(dilated)
    
    binary = dilated > (thresh+0.0005)
    
   # plt.imshow(binary)
    #plt.show()
    labelled_image = measure.label(binary, background=None)
    properties = measure.regionprops(labelled_image)
    
        #print labelled_image
        
      #  pylab.imshow(labelled_image)
    
    

    
    new_photo_name= "".join(str(dir_output+photo.split(".")[0] + "_converted" +".JPG"))


    #I save the image that was counted to a folder so it can be checked and compared against original image
    
    mpimg.imsave(new_photo_name, binary)
    
    object_areas=[prop.area for prop in properties]
    object_perimeter=[prop.perimeter for prop in properties]
    
    #find R from area

    from math import pi
    radii=[(x/pi)**0.5 for x in object_areas]
    
    pairs=[object_perimeter,radii]
    
    
    circles=[x/(2*y) for x,y in zip(object_perimeter, radii)]
    #circles=[x for x in circle if x >3.0 and x<3.28]
    
    new_area=[]
    new_perimeter=[]
    circle2=[]
    for areas,circs in zip(object_areas, circles):
        if circs > 2.6 and circs < 3.58:
            circle2.append(circs)
            new_area.append(areas)
            new_perimeter.append(circs)    
       
    seed_count=len(circles) 

#NOW APPLY A SIZE THRESHOLD CUTOFF


    new_area.sort()
  #  print new_area
    index=int((len(new_area)*(0.75)))-1
    median_cutoff=2.25*new_area[index]


# removes small objects depending on the number of objets in the image a different size filter is applied
    if len(new_area)>40:
        min_cutoff=0.1*new_area[int(len(new_area)*0.67)]
        
    elif len(new_area)<41 and len(new_area)>16:    
        #take the middle 5 observations 

        min_cutoff_index=int(len(new_area)*0.25)
                   
        min_cutoff=new_area[min_cutoff_index]
        
        #remove lowest value and check mean, remove any items that cause huge jump in mean seed area. 
        mean1=sum(new_area)/len(new_area)
        z=0
        for i in new_area[:-1]:
            z+=1
            temp_area=new_area[z:]
            mean2=sum(temp_area)/len(temp_area)
            #print mean1, mean2, mean1-mean2

            if mean2-mean1<6:
               # print temp_area
                #print new_area
                break
            
            mean1=mean2

        min_cutoff=new_area[z-1]
        
    else:
        min_cutoff=10
    #if the difference between the maximum object size  and the median object size is more than twice the median size that the max cutoff is 3 times the median
    #else there is no need to apply a max cutoff and 
    if max(new_area)-median_cutoff > (2.0* new_area[index]):
        max_cutoff=3*new_area[index]
    else:
        max_cutoff=max(new_area)


    seed_count=(sum([1 for x in new_area if x >= (min_cutoff) and x<= max_cutoff]))
    #find max area of the objects and ask is it more than twice the size of what I would count as 2 seeds 
    
    double_seeds=sum([1 for x in new_area if x > max_cutoff and x<1000])
    
    seed_count=seed_count+ double_seeds
    
  #  seed_count3=(sum([1 for x in object_areas if x> median_cutoff and x<max_cutoff]))
  
#add more seeds to correct for seeds touching

    
    old_photo_name= "".join(str(dir_input+photo))
    
    date_taken= time.ctime(os.path.getmtime(old_photo_name)).split()
    date_taken1= " ".join([date_taken[1], date_taken[2],date_taken[4]])
    #x=[date_taken1, photo,seed_count,seed_count2,seed_count3,object_areas]
  #  x=[date_taken1, photo,seed_count,seed_count2,seed_count2+seed_count3, (variance2)**0.5]
    x=[date_taken1, photo,seed_count]
    
    
    object_areas.sort()
    x=[date_taken1, photo,seed_count,len(object_areas),object_areas]
    
    x2=map(str,x)
    
    print ",".join(x2)
    
    #Here I make a list of photos that are likely to have problems
    if max(new_area)-max_cutoff>550:
       # print ",".join(x2)        
        x2=",".join(x2)
        sys.stderr.write(x2)
   

    
sys.stderr.close()


