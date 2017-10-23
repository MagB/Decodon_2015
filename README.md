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
Figures along with scripts that generated them are housed in the folder called "figures_w_scripts".
Tables along with scripts that generated them are housed in the folder called "tables_w_scripts".



### Folders:
1. data: contains 3 folders: 
* field_data (raw data collected from field such as seed counts, ramet and population level observations, also includes scans of MPB field books) 
* old_intermediate_files (old merged data files that are now obsolete, not needed or have been updated)
* output_data (contains any merged,cleaned or formatted data) this is data that is ready for analysis.
2. field_work_2015: contains any documents CT shared with MPB during field work, field photos and misc information pertaining to conducting field surveys. 
3. figures_w_scripts: contains folders for each figure. Each folder will house the script that generated the figure along with the resulting figure.
4. python_unix_scripts: custom scripts written by MPB, currently (oct 2017) used for automating seed counting of seed photos
5. references: references for analytics or papers that may be difficult to find again
6. scripts: houses the R scripts used for data cleanup, wrangling, and analysis  
7. tables_w_scripts: tables along with scripts generating them
8. Seed_counting: this is a compressed folder that contains the seed photos and scripts used to count seeds. MPB validated the seed counts from the photos in oct 2017. In 
many instances seeds were hand counted or re-classified. 
 
### Data Description:
In this project, there is information  populations surveyed by MPB and CT in 2015. 
There is also two datasets pertaining to the greenhouse collection of D. verticillatus.
 
There are 4 field datasets currently part of this project: 
1. Decodon_population_survey_2015_by_MPB_CT.csv: Survey of D. verticillatus populations across Ontario and Quebec (one location). This includes morph frequency estimate.
2. Decodon_population_flowering_fruiting_2015.csv: Population-level estimate of fertility (proportion of fruiting and flowering ramets)
3. Decodon_ramet_observations_2015.csv: Ramet-level estimates of fertility: number of flowers and fruits per ramet (of ramets that made at least one flower).  
4. Decodon_field_seed_counts_2015.csv: Ramet-level estimate of fertility based on seed counts from field collected fruit (collected in October 2015 by MPB). Several undergrad volunteers helped count seeds.

### How to use the data:
The two ramet level datasets described above in "Data Description" have been cleaned, verified and merged into a single file (seed data was joined to flowers and fruit data)
The cleaned and merged data are located in  the "data/output_data/"  folder. For analysis of ramet level fertility, use the data files located in the  "data/output_data/" folder.

The two other datasetets : 1. Decodon_population_flowering_fruiting_2015.csv and 2. Decodon_population_survey_2015_by_MPB_CT.csv are good to use for analysis as they are.


### Data Analysis Performed to Date:
All figures and tables are housed in their own folder along with the script that generated them.

### 1: Map of populations surveyed in 2014 & 2015, as well as a map of 24 samples used in RNAseq
In the folder called "figures_w_scripts" you will find folders for each figure. Each folder will house the script that generated the figure along with the resulting figure.

There are 36 populations in total that have been identified by members of the lab. This map, however, only includes the 27 unique sites where plants were sampled in 2015. Flowers, pollen, leaf tissue and live plants were collected from 22 sites (20 unique sites) in 2015. 
Seeds were collected from all but one of these populations (Puslinch). Seeds were collected from an additional 7 sites for which live plants had been collected in 2014.

###  Current Tables:
Table1. Summary table of morph frequencies for all populations for which data is available.
located:
Decodon_2015/tables_w_scripts/Table1_morph_frequencies/Table1_summary_of_morph_frequencies.csv

Table2. Summary of the proportion of ramets with flowers and fruits. This table provides a weighted proportion. Several sites within each population were surveyed.
Each site is at least 16 ft apart. A site is defined at the area between the length of a 16ft canoe/kayak to the shoreline. At each site MPB estimated the proportion of ramets that had flowered and that may have produced fruits. 
This survey was conducted in Oct 2015. MPB was unaware that Decodon aborts flowers. Thus, the estimate of flowering is underestimated in all populations and the proportion of fruiting ramets for flowering ramets (along with the ramet level estimate of fruits per flower) 
are all overestimated. 
located:
/Decodon_2015/tables_w_scripts/Table2_proportion_frt_flr/Table2_Proportion_frt_flr.csv

Table 3. Summary statistics for each population and morphs of fertility traits 

** Secondary_branches: The number of secondary branches on each ramet was also counted. Secondary branches were counted if there were fruits present or the branch was longer than ~5cm. 
Flower_num: For each ramet the remaining flowers (fertilized and unfertilized) present in oct 2015 were counted.
Frt_flr: number of fruits per flower. denominator is the corrected fruit number described below.
Seeds_per_fruit_corrected: This is an estimate of seeds per fruit but using the corrected number of fruits in the denominator
Fruit_num_corrected: For each ramet the number of fruit produced was counted in the field in oct 2015. Several fruits from each ramet were collected for seed counts. In some cases the fruits collected by MPB turned out not to be fruits.
This trait corrects the number of fruits counted in the field to account for those that were not real fruits. 
located:
/Decodon_2015/tables_w_scripts/Table3_pop_means_ramet_fertility/Table3b_morph_means.csv

###  Current Figures:

Figure 1. Population map
There are two maps for Figure 1. The first is a map of all the surveyed populations. The second is a map of only the 24 populations that are included in the RNAseq study.
located:
/Decodon_2015/figures_w_scripts/Figure1_pop_map/Morph map_oct2017.eps
/Decodon_2015/figures_w_scripts/Figure1_b_pop_map_RNA_seq/Morph_map_RNAseq_oct2017.eps


Figure 2. Percentage of flowering and fruiting ramets in each population ordered from south to north.
located:
/Decodon_2015/figures_w_scripts/Figure2_prop_frt_flr/Figure2_prop_frt_flr.eps 


Figure 3. Summary of fertility based on fruits (Figure 3a) and seeds (Figure 3b)
The pattern observed for flower number is nearly identical to that of fruit number. Thus, only the data for fruit number is shown. This is most likely due to the bias in how the data were collected.
Flowers and Fruits were counted in october. Because decodon aborts many flowers, the number of flowers per ramet is likely grossly underestimated. MPB did not know 
about flower abortion in decodon. MPB mistakenly assumed that dehisced flowers were mostly retained on the stem as is the case in L. cardinalis. 
This is an important lesson in knowing your organism before collecting data.
Compared to the six most southerly polymorphic populations, the monomorphic populations tended to produce fewer fruits per flowering ramet. 
The more northerly polymorphic populations, however, exhibit a reduction in numbers of fruits produced per ramet, wherease the monomorphic populaitons do not show a consistent decrease with latitude. This suggests that some ecological factor may be liiting fruit production in northerly populations, but that investment in sexual structures like flowers and fruits differs between monomorphic and polymorphic populations. 
located:
/Decodon/Decodon_2015/figures_w_scripts/Figure3_fertility_fruit_seed/Figure3a_fertility_fruit.eps
/Decodon/Decodon_2015/figures_w_scripts/Figure3_fertility_fruit_seed/Figure3b_fertility_seeds.eps


