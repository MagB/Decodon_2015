



# This folder contains 10 datasets and a folder called “output_data”

1. Decodon_cold_storage_2016.xls 
2. Decodon_greenhouse_2016.xlsx
3. Decodon_population_fruiting_2015.xls
4. Decodon_ramet_observations_2015.xls
5. Decodon_seed_photos_labels_and_hand_counts.xlsx
6. Decodon_population_survey_2015_by_MPB_CT.xls
7. Seed_count_June8_night_2016_no_bad_photo3.txt
8. Seed_count_June8_night_2016_no_bad_photo3_no_areas.txt
9. Seed_count_June8_night_2016_no_bad_photo3_no_areas.txt
10. Seed_count_June8_night_2016_no_bad_photo3.txt


### output_data folder: houses any merged and manipulated data files. Currently, this folder has 3 dataset:
1. Decodon_ramet_observations_2015_merged_w_seed_counts.csv2. Decodon_seed_counts_hand_and_photo.csv3. pop_by_fertility.csv

####1. Decodon_ramet_observations_2015_merged_w_seed_counts.csv
This dataset has ramet level data. It contains the PopCode, Lat, Long, frequency of  L, M and S, #of flowers/ramet and # fruits/ramet. It also contains information about the seed counts per fruit.

####2. Decodon_seed_counts_hand_and_photo.csv
This dataset was created by a script called “Merging_hand_and_photo_seed_counts.R “ 
This dataset has both hand counts and the few hundred photo analysis counts merged together for each fruit/envelope.

####3. pop_by_fertility.csv
This dataset has the summary (means) of main fertility estimates. This dataset is used to identify high and low fertility pops for the mating design.

# Main data folder:
####1. Decodon_cold_storage_2016.xls
This dataset contains a list of all plants collected as clonal offshoots or cuttings in 2014 by C. Eckert and in 2015 by MPB and CT.
It lists the original popcode given to the "baby plants" ie. NO.ON.M1  
These Plant_ID tags are all the original tags assigned to the plants

* Column names:description
* Date_moved: mm/dd/yr	
* Plant_ID: ID on tag
* Tray: First set of plants moved I kept track of position
* NOTES

####2. GH_pops_2016.xlsx
These are plants that were taken out of coldstorage and placed into the greenhouse in March  and April of 2016. Plants moved in March were used for RNA extractions.

* PopCode2: population identifier
* Plant_ID: individual plant identifier
* GH_try: this is the greenhouse tray location of the plant (trays 1 - 15)	
* Date: Date the plant was moved to GH
* Devel_Stage: categorical number assigned to developmental stage by Michael during the week of Jul 1 2016. Stages range from 0- 8, with 0 being no sign of recovery, 8 fully opened flowers
* Notes: any anomalies that need to be examined
* Notes2: this column just indicates if the plant was possibly used for RNA 

####3. Decodon_population_flowering_fruiting_2015
Each record represents a site surveyed in a population in Oct 2015 by MPB. Surveys were done at least 1 boat length apart and included all plants within the length of the canoe to the shoreline. 

* Date: date of observations
* Pop_ID: Main identifier for ON region (includes NO sites)
* PopCode: original pop codes given in field
* PopCode2: pop codes updated for NO.M1 NO.M2 and NO.D1 (changed to ON region codes)
* Site_number: in some pops that had large area covered by decodon I kept track of which site I was collecting data. 
* PopName: Lake or community name
* Prop_stems_flowering: proportion of stems(ramets) that had at least one flower 
* Prop_stems_fruiting: proportion of stems/ramets that had at least 1 fruit (or looked like a fruit, typically I checked fruits that I thought might be empty by tearing open a few to check for seeds, as long as a fruit had a seed I considered it a fruit)
* Clump_num: when estimating number of ramets observed I kept track of the number of clumps within the boat-to-shore area in many pops decodon grew in defined clumps
* Stems_per_clump_min: when growing in clumps I estimated clump number and min-max # ramets per clump to estimate total stem number in area
* Stems_per_clump_max
* Total_stems_in_area: When I couldn't define clumps then total stem estimate for site was recorded. For sites with defined clumps, total_stems are estimated as the minimum number of stems per clump* number of clumps.


####4. Decodon_population_survey_2015_by_MPB_CT.xls
This contains basic pop data of all populations surveyed by MPB and CT. It also includes pops that were surveyed by Eckert in 2014 and had samples of those pops growing in the greenhouse in 2015/2016. Some of the Eckert collected plants also had leaf samples collected (CT collected and labelled these )
Most pops in this set also were visited in 2015 for floral morphing and/or seed collections. 

* Region_code: used original code EO, ON and NO	
* Type: Monomorphic, Di- or Trimorphic
* Pop_ID: this is pop code with RegionCode stripped
* PopCode: original popcode given by CT and MPB in field
* PopCode2: corrected popcode so the 3 NO pops now have ON
* PopName: Lake or community names
* Region_name: district names
* Province:
* Date_FLRS_Surveyed: date on which floral morphs were assessed in field by CT and MPB	
* L: count of Long morphs	
* M	
* S	
* Lat	
* Long	
* Pop_Size_Field_Estimate_2015: estimate of pop size based on ramet number
* Pop_size_Estimate: estimate of pop size based on ramet number but in purely numerical format 
* Prop_stems_w_buds_2015_notes: 
* Prop_stems_w_buds_2015: proporiton of stems in pop with buds (should be close to proportion of flowering stems in pop)
* Prop_stems_w_open_flr_2015_notes	
* Num_LivePlantsGrowing_2015: number of live plants growing in GH from that pop
* Year_Live_Plants_Collected	
* Num_SampledForLeaves_2015	
* Num_SampledForFlowers	
* SampledForSeeds; y or n to indicate whether we have collected seeds from this population	
* Flrs_Sampled_Maggie_Corrina:indicates if floral morph was assessed by MPB and CT
* Notes1	
* Notes2


####5. Decodon_ramet_observations_2015.xls
Information on every ramet from which seeds were collected is recorded in this dataset. From each ramet I collected ~5 fruits. These were all placed into a single envlope which was labelled with the population (the popName) date collected, and number of flowers and fruits on that ramet. Secondary branches larger than 10cm were also noted. 
When possible the number of ramets in the clump that the focal ramet was located was recorded (clump_size_)

* Envelope_ID	
* PopName	
* Pop_ID	
* PopCode	
* PopCode2	
* Date_collected: dd/mm/yr
* stems	
* Clump_size	
* Flower_number	
* Fruit_number	
* Secondary_branches	
* Notes	
* Seed number


####6. Decodon_seed_photos_labels_and_hand_counts.xlsx
Undergrad volunteers: Vivienne Wu, Kathlein Wei Cheng, Rebecca Huang, Sierra Klueppel, Michael Ramnauth 
Each seed envelope for which fruits were opened and seeds counted is recorded in this dataset. Seeds were counted in one of two methods: 1. hand counting (this data is recorded directly in this dataset) or 2. seeds were photographed and processed using image analysis (a custom python script written by MPB). The hand written data is housed in the black binder in the section called “Seed Counts”. This binder is kept either in the lab beside Decodon field collected seeds (from 2015) or above MPB’s desk. 
This data is merged with the Seed_count_June8_night_2016_no_bad_photo3.txt (counts of image analysis) to produce the complete seed count data "/Users/Maggie/Documents/Decodon/Decodon_2015/data/output_data/Decodon_seed_counts_hand_and_photo.csv"


*Page	: page of written observations in black binder
*Photo_num :if more than one photo was taken for an item then the item is represented in two rows and Photo_num is P1 and P2 for each row	
*Date: Date the envelope was processed
*Person_ID: Person who processed the enveloped	
*Photo	: Y or N , indicates if Seed_number is based on hand or image counts
*Envelope_ID: Each envelope with fruit is numbered with a haphazardly assigned number so that counting is done blind to population 
*Fruit_ID: For most envelopes we counted seeds from 5 fruits and recorded for each fruit separately. If fruits opened in the envelope then we counted all seeds for all fruits that had opened. In this case fruit_ID is 1-5 to indicate this is the seed count for 5 fruits. 
*Seed_number	
*NonViable_seeds: Y or N, record of whether inviable/aborted seeds were observed by counter
*Notes: most common note is what kind of aborted seeds were observed (early: look like dust but have shape of seeds, mid: very small ~1-2mm seed shaped late: these were formed seeds but were small dark black/brown and had “craters”
*Notes2			


#### 7. Seed_count_June8_night_2016_no_bad_photo3.txt
This is the output from the python script “Decodon_seed_counts_circle_correction2.py”. This script takes in a list of folders containing seed photos, converts them to binary images and counts objects in image with a shape and size correction on the objects. This script works incredibly well for photos with more than 10 seeds, but has a high error rate for few seeds. This could be corrected, but would require more investment of time. Because we found that for the majority of seed envelopes we became faster doing hand counts we chose to abandon the seed photo count method. Only 256 fruits/seed envelopes were counted using photo analysis. 
This data does not have column headers.
The columns of this data set are:
Date_taken: Date photo was taken
Photo_ID: Photo IMG_# assigned by camera
Seed_count_corrected: seed count from python script with filter applied
Object_count: count of all objects pre-filteringList_of_object_areas: list of areas of all objects pre-filtering


#### 8. Seed_count_June8_night_2016_no_bad_photo3_no_areas.txt
This dataset is just a reduced dataset (first 4 columns) from the Seed_count_June8_night_2016_no_bad_photo3.txt 
It is this dataset we use in the R script called “Merging_hand_and_photo_seed_counts.R