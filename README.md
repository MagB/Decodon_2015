# Reproductive Ecology and Genetics of Decodon verticillatus: general workflow and project management

## Overview
The way organisms reproduce not only dictates their Darwinian fitness but also controls the
movement of genes in time and space. Reproductive traits are expected to be under very strong
selection and evolutionary shifts in reproduction should have several consequences for how genetic
variation is distributed within and among populations, and hence the capacity for evolutionary
adaptation in rapidly changing environments. More than 70% of angiosperms engage in clonal
reproduction at some stage of their lifecycle, but little is known about the relative importance of
asexual vs. sexual reproduction in natural populations. There are a handful of studies that show that
asexual lineages (at least within North America) tend to occur further to the north at the periphery of
species ranges, suggesting that asexual recruitment may be favored in harsher environments. With
quickly changing environmental conditions, populations at range margins might be expected to be
hotspots of adaptation, but asexual reproduction may reduce the adaptive potential of these populations.

Throughout much of its geographic range, Decodon verticillatus reproduces sexually as well as clonally (via adventitious rooting). 
D. verticillatus is a tristlyous (with short, long and mid-length stigma positions), perennial common to wetland habitats throughout eastern-central North America. Unlike most tristylous species, D. verticillatus
is self-compatible, but incapable of autogamous self-fertilization. Populations show variance in morph frequency. While most southern and central 
populations tend to contain all three morphs, those towards the northern periphery of the species range tend to be monomorphic (Eckert and Barrett 1992).
Because tristyly in this species is controlled by two loci with dominance, even low levels of sexual recruitment would result in the presence of more than one floral morph. 
Thus, monomorphic populations likely result from severe reductions in sexual reproduction (Eckert and Barrett 1993). 


In this study, we address hypotheses about how vestigialization of sexual traits—a common phenomenon, present across plant and animal taxa—occurs
in nature.  Genomic tools will open new avenues to explore whether vestigialization of sexual traits results from drift (relaxed
selection allowing mutations to accumulate) or if selection favoring asexual recruitment also selects for
reduced or modified trait expression. This will be the first study to directly compare how genetic
diversity is shaped by different levels of sexual recruitment in natural populations, and specifically test
hypotheses regarding the loss/reduction of sexual traits.


## The proximate goals of the current project are to:
1. Find new Decodon populations across the northern periphery of the species range.
2. Document fertility in the wild of populations across the northern periphery of the species range 
system Monomorphism is thought to be the result of a reduction in sexual reproduction.   
the distribution of morph type across
3. Validate that any loss of fertility observed in the wild has a genetic basis by conducting greenhouse crosses. From each population surveyed in the wild, live clonal offshoots were collected and transported back to 
Queen's where they were grown in the glasshouse (second last glasshouse). Plants were taken through one season of overwintering in cold storage rooms and cold growth chambers kept at 4C.
In April of 2016, plants were brought out of cold storage, repotted in Promix potting soil and placed in the glasshouse. These plants were used in the crossing experiment and provided fresh tissue
for the RNA-seq project. 
4. Develop SNP markers using RNA-seq to quantify patterns of genetic diversity in monomorphic versus tristylous and distylous populations. Twelve monomorphic populations
that were likely to be clonal with low fertility in nature and twelve high fertility populations (di and tristylous) were selected for RNA-seq. This portion of the project is ongoing. 
RNA was successfully extracted by MPB. Tissue was collected from plants grown in the glasshouse (taken through at least 1 season of cold storage). We standardized the developmental stage of the tissue collected by only choosing
the youngest leaf tissue from plants whose primary branch was no greater than 1m was used. RNA was extracted using Qiagen RNeasy plant RNA extraction kit. On-column DNA digest was also performed using RNase-Free DNase (Qiagen Catalog No. 79254).
RNA samples were sent to Genome Quebec for RNA-seq.For each sample a NEB/KAPA mRNA stranded Library was created at Genome Quebec (Montreal QC) and RNA was sequenced using the Illumina HiSeq 2500 paired-end 125bp sequencing platform. 

## Project structure layout
Each folder will contain a README.md file (whenever appropriate) that describes the contents of that folder in more detail. 

### Folders:
1. data: contains 3 folders: 
* field_data (raw data collected from field such as seed counts, ramet and population level observations, also includes scans of MPB field books) 
* old_intermediate_files (old merged data files that are now obsolete, not needed or have been updated)
* output_data (contains any merged,cleaned or formatted data) this is data that is ready for analysis.
2. field_work_2015: contains any documents CT shared with MPB during field work, field photos and misc information pertaining to conducting field surveys. 
3. output: houses figures and merged data sets. This may change. 
4. python_unix_scripts: custom scripts written by MPB, currently (oct 2017) used for automating seed counting of seed photos
5. references: references for analytics or papers that may be difficult to find again
6. scripts: houses the R scripts used for data cleanup, wrangling, analysis and plotting 
7. Seed_counting: this is a compressed folder that contains the seed photos and scripts used to count seeds. MPB validated the seed counts from the photos in oct 2017. In 
many instances seeds were hand counted or re-classified. 
 
### Data Description:
In this project, there is information  populations surveyed by MPB and CT in 2015. 
There is also two datasets pertaining to the greenhouse collection of D. verticillatus.
 
There are 3 types of field data currently part of this project: 
1. Survey of D. verticillatus populations across Ontario and Quebec (one location). This includes morph frequency estimate.
2. Population-level estimate of fertility (proportion of fruiting and flowering ramets)
3. Ramet-level estimates of fertility (currently this is limited to number of flowers and fruits per ramet, of ramets that made at least one flower).  
4. Ramet-level estimate of fertility based on seed counts from field collected fruit (collected in October 2015 by MPB). Several undergrad volunteers helped count seeds.


### Data Analysis Performed to Date:

### 1: Map of population survey conducted in 2015
Script: “population maps2.R" 

This script is used to map the location of Decodon sites. This is housed in the folder named "scripts".
There are 36 populations in total that have been identified by members of the lab. This map, however, only includes the 27 unique sites where plants were sampled in 2015. Flowers, pollen, leaf tissue and live plants were collected from 22 sites (20 unique sites) in 2015. Seeds were collected from all but one of these populations (Puslinch). Seeds were collected from an additional 7 sites for which live plants had been collected in 2014.
Decodon is a tristylous species (Long-style, Short-style and Mid-style), but populations can be composed of one or more morphs. 

### Part2: Summary statistics of fitness related traits for populations surveyed by MPB and CT in 2015. 
Script: Summary_statistics_w_xlsx_files.R (don’t use Summary_statistics.R, that script was a first pass and used .ods data sheets as data input)

We have information on 26 unique populations. 20 of these populations have frequencies of floral morphs collected in 2015 (note that the Rice lake and Jock River populations have two sites surveyed, but should be considered one population). 8 additional populations have floral data that were collected by previous members of the Ecker lab (MPB did not validate those data).

First, this script calculates the number of plants for which floral morph-type was documented (data collected by CT and MPB 2015). Second, this script calculates basic summary statistics like the mean, median, min and max of ramet-level fertility estimates.  
There is a difference in fertility between this survey and that reported in Dorken and Eckert 2001.
The magnitude of the difference between monomorphic and non-monomorphic populations for number of flowers, fruits and fruits per flowers is smaller in 2015 than that reported in 2001. More strikingly, the average number of fruits per flower in 2015 in the monorphic populations is greater than that reported for trimorphic populations in 2011.

Note: the script used to calculate the various summary statistics is organized into functions. There is some description on how to properly call those functions, but more detailed notes are likely needed to complete this script. Also, some changes may be needed to handle the morphological data when it becomes available.
/Users/Maggie/Documents/Decodon/Decodon_2015/README.md


### Part3: 
Scripts= Population_level_fertility.R + Modelling_fertility_w_plots.R 

This section begins to explore the fertility data. I plot the mean flower and fruits per ramet (that had at least one flower) and the proportion of fruiting and flowering ramjets.

This section uses 2 scripts:

Population-level fertility: 
+  script= Population_level_fertility.R.
+ dataset= "Decodon_population_flowering_fruiting_2015.xls"
This script looks at the percentage of fruiting and flowering ramets in a population. This gives the best approximation of population level fertility. Two plots each with 2 panels (one for fruiting and one for flowering) are made using this script. One figure is the percentage of ramets in a population that produced flowers/fruits. The other figure is the percentage of ramets flowering/fruiting by population type (monomorphic and polymorphic-includes D and T pops)

Ramet-level fertility:
+ script=Modelling_fertility_w_plots.R 
+ dataset= "/Users/Maggie/Documents/Decodon/Decodon_2015/data/Decodon_ramet_observations_2015.xls”,1)"
This script models the ramet level fertility. Only ramets that had at least 1 flower are included in these data. It is possible that flowering ramets produced no flowers, but non-flowering ramets are not included here.   
Two 2-panel plots are made using this script, as well as some preliminary models of fertility by populaiton and populatoin type. The first plot shows the number of flowers (top panel)/fruits(bottom panel)produced per ramet for each population. The other plot shows the number of flowers(top panel)/fruits(bottom panel) produced per ramet for monomorphic and polymorphic populations. 

