# Description of folders and data

This folder contains 4 data files which describe data collected from a field survey of Decodon verticillatus populations conducted by MPB and CT during summer-fall of 2015. 
The folder called “Field_books_2015” contains the scanned images of MPB’s field books. Book #1 contains the population information (GPS coordinates, location and description), along with an estimate of the number of ramets, and record of morph frequency. 
Book #2 contains information about proportion flowering, number of stems, proportion fruiting etc.

# Data file list:
1. Decodon_field_seed_counts_2015.csv
2. Decodon_population_flowering_fruiting_2015.csv
3. Decodon_population_survey_2015_by_MPB_CT.csv
4. Decodon_ramet_observations_2015.csv


# Data file description:

# 1. Decodon_field_seed_counts_2015.csv
Undergrad volunteers who helped count seeds: Vivienne Wu, Kathlein Wei Cheng, Rebecca Huang, Sierra Klueppel, Michael Ramnauth 

In October 2015, MPB visited several populations. MPB collected fruits from each ramet that had any fruits or dried flowers that looked like they might have a seed. 
MPB collected multiple fruits from each ramet into a single envelope. Each envelope was given a random number so that seed counting would be done blind with respect to population. 
In many cases, fruits remained intact in the envelope. In these cases, up to five fruits were chosen and seeds within each fruit were counted. Thus, one envelope may have upwards of 5 rows, 1 for each fruit.
In other instances seeds had fallen out of fruit and thus seed count for each fruit could not be obtained. In this scenario, the number of fruit counted e.g., 1-9 (means 9 fruits were counted) and the total seeds recorded for all nine fruit. 
In a few instances, we could could seeds for a few fruits individually but had to count a group of fruits. For eg., Envelope 356 may have fruit 1-3 with a seed count and fruits 4 and fruit 5 have individual seed count. This was done, so that 
variance in seed number among fruit within a ramet could be calculated whenever possible. 


## Seeds were counted in one of two methods: 
1. hand counting (this data is recorded directly in this dataset) 
2. photography:seeds were photographed and processed using image analysis (a custom python script written by MPB). The hand written data is housed in the black binder in the section called “Seed Counts”. This binder is kept either in the lab beside Decodon field collected seeds (from 2015) or above MPB’s desk. 
the estimate of seed counts for photographed seeds is reported in the "Seed_count_June8_night_2016_no_bad_photo3.txt “ file. This is housed:
/Users/Maggie/Documents/Decodon/Decodon_2015/data/old_intermediate_files/Seed_count_June8_night_2016_no_bad_photo3_no_areas.txt
It is located int the "old_intermediate_files" folder because it is an intermediate file that is merged onto the file of hand counts.

Note that all photographed seed counts were validated by MPB. This involved comparing seeds counts with the photos to ensure the right "ballpark" number was recorded. Also, MPB ensured that all photographed seeds were counted as "viable"
We only counted seeds that appeared viable for the seed count. Viable was defined as being plump, but not necessarily being large. There was quite a lot of variation in seed size and colour. Seeds that were dark, but plump were considered viable.
Seeds that were small but well shaped were also counted as viable. "unviable" seeds were considered those that looked flattened, almost as if someone had sucked the insides out of the seed. 
In these cases we call those "late stage aborted". I wanted to keep track of fruits that were pollinated even if they did not result in "good" "viable" seeds. 
It must be acknowledged however that "viability" here is a guess. A germination trial is needed to verify if seeds are indeed duds.


## Column description:
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

2. Decodon_population_flowering_fruiting_2015
In each population, MPB surveyed a “site”. A site is defined as the area from the canoe to the shoreline within the front and end of a 16ft research canoe. Each record represents a site surveyed in a population in Oct 2015 by MPB. Surveys were done at least 1 boat length apart and included all plants within the length of the canoe to the shoreline. 

## Column description:
* Date: date of observations
* Pop_ID: Main identifier for ON region (includes NO sites)
* PopCode: original pop codes given in field (note that CT originally assigned some populations NO for northern ontario rather than ON, the three NO populations’ id was subsequently changed to be inline with the other ontario pop codes) 
* PopCode2: pop codes updated for NO.M1 NO.M2 and NO.D1 (changed to ON region codes)
* Site_number: in some pops that had large area covered by decodon I kept track of which site I was collecting data. 
* PopName: Lake or community name
* Prop_stems_flowering: proportion of stems(ramets) in a site that had at least one flower. For example, if MPB estimated there to be about 100 ramets from the boat to the shore and half had flowers remaining Prop_stems_flowering=50)
* Prop_stems_fruiting: proportion of stems/ramets that had at least 1 fruit (or looked like a fruit, typically I checked fruits that I thought might be empty by tearing open a few to check for seeds, as long as a fruit had a seed I considered it a fruit)
* Clump_num: when estimating number of ramets observed I kept track of the number of clumps present from within the boat-to-shore area. In many pops decodon grew in defined clumps and in others clumps (which are probably genets) could not be differentiated from one another. It just looked like a bunch of ramets.
* Stems_per_clump_min: when growing in clumps I estimated clump number and min-max # ramets per clump to estimate total stem number in area
* Stems_per_clump_max
* Total_stems_in_area: When I couldn't define clumps then total stem estimate for site was recorded. For sites with defined clumps, total_stems are estimated as the minimum number of stems per clump* number of clumps.

# 3. Decodon_population_survey_2015_by_MPB_CT.csv
This contains basic pop data of all populations surveyed by MPB and CT. It also includes pops that were surveyed by Eckert in 2014 and had samples of those pops growing in the greenhouse in 2015/2016. Some of the Eckert collected plants also had leaf samples collected (CT collected and labelled these )
Most pops in this set also were visited in 2015 for floral morphing and/or seed collections. 


## Column description:
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

## 4. Decodon_ramet_observations_2015.csv
Information on every ramet from which seeds were collected is recorded in this dataset. From each ramet I collected ~5 fruits. These were all placed into a single envlope which was labelled with the population (the popName) date collected, and number of flowers and fruits on that ramet. 
Secondary branches larger than 10cm were also noted. 
When possible the number of ramets in the clump that the focal ramet was located was recorded (clump_size_)

* Envelope_ID: this is the random number assigned to the envelope so that seed counting could be done blind to population
* PopName: pop identifier
* Pop_ID: pop identifier
* PopCode: pop identifier
* PopCode2: pop identifier
* Date_collected: dd/mm/yr
* stems: this identifies the main branch. In a few cases, the ramet branched from one common stock that came out of the water. These are id'd as stema and stemb
* Clump_size: in some pops ramets grew in close clumps. whenever possible we recorded the size of the clump this particular ramet came from .
* Fruit_number: number of flowers and/or scars remaining on ramet
* Secondary_branches: number of branches larger than 10cm coming off main branch
* Notes:
* Seed number: in a few cases seeds were counted for these envelopes right away.
