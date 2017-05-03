# Denver 2016 B-cycle Ridership Data Exploration

![](https://github.com/hbhasin/Capstone-Project-1/blob/master/data/Denver%20B-cycle.PNG)

[Denver B-cycle](https://denver.bcycle.com/) is a non-profit public bike sharing organization operating an automated bike sharing system called Denver B-cycle. Its mission is to "serve as a catalyst to fundamentally transform public thinking and behavior by operating a bike sharing system in Denver to enhance mobility while promoting all aspects of sustainability: quality of life, equity, the environment, economic development, and public health" its purpose, its organization and discuss its relevance to this exploration.

Denver B-cycle posts its trips data set on its website as soon as its annual report is released. Trips data have been available since 2010. The 2016 annual report and its associated dataset for this report were obtained from [Denver B-Cycle website.](https://denver.bcycle.com/). The original plan was to use the 2015 dataset to continue the effort by Tyler Byler who published a report, [Exploring 2014 Denver B-cycle Ridership](http://datawrangl.com/2016/02/21/denver-bcycle/). In his study Tyler indicated that “most calendar and clock variables were highly significant when predicting ridership, and weather variables such as temperature and amount of cloud cover appear to be as well”. The original plan for this report was to use 2015 data to continue Tyler’s work. However, the 2016 data became available at the end of February 2017, so gears had to be rapidly shifted to use this data instead. To this end, the reporting style will follow Tyler's study to provide seamless continuity and good reference on trends and analyses.

This study has three parts:
1.	Explore the Trips datasets and visualize the data to provide useful and interesting information.
2.	Deploy a variety of regression models to train and test the data.
3.	Deploy a variety of classification models to train and test the data.

# Part 1: Data Exploration

## Data Acquisition

Data for this study was downloaded from several sources and combined using the following steps:
1.	Downloaded B-cycle 2016 Trips and Kiosk data from [Denver B-Cycle website](https://www.denverbcycle.com/company). The columns names were changed to comply with Python code best practices.
2.	Created a list of the 7921 combinations of the 89 checkout/return kiosks. Used [Google Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/) to provide the bicycling distance and time between each checkout and return kiosk. Adopted Tyler’s method of finding the average distance by taking the distance from each checkout-return pair’s distance separately then averaging it. As he pointed out in his study, this approach was taken “because of the large number of one-way streets in the Denver downtown area where the kiosks are highly clustered”. Google only supports a maximum of 2500 requests a day, it took four days to obtain this data.
3.	Obtained daily and hourly weather data via [Dark Sky API](https://darksky.net/dev/) for all of 2016. Dark Sky supports up to 1000 requests per day

### Basic Ridership Statistics 
#### Number of Rides 
The B-cycle data, as downloaded, contained 419,611 rows of trips data. Under normal circumstances this would mean that 419,611 B-cycle trips were taken in 2016. However, the [2016 Denver B-cycle annual report](http://denver.bcycle.com/docs/librariesprovider34/default-document-library/dbs_annualreport_2016_05.pdf) acknowledged 354,652 total trips for the year. The breakdown was as follows:
