import sys
import datetime

my_photos=open("/Users/Maggie/Documents/Decodon/Decodon_2015/output/seed_count_June8_2016.txt3", 'r')
#my_photos2=open("/Users/Maggie/Documents/Decodon/Decodon_2015/data/Decodon_seed_photos_labels_and_hand_counts.csv", 'r')

for line in my_photos:
    if line[0]=="P":
        continue
    sline1=line.rstrip("]\n")
    sline2= sline1.split(",")
    
    date_photo=sline2[1].split("-")
    date_photo=map(int,date_photo)
 #   date_photo=sline3[0]
    formated_date_photo = datetime.date(date_photo[2], date_photo[1],date_photo[0])
    print formated_date_photo
    
    
    