## Capstone-Project-1
# Denver 2016 Bike Share

### Project Summary
This project was undertaken to fulfill one of the two Capstone projects required by [SpringBoard.com](https://springboard.com). It explores the Denver 2016 Bike Share Trips dataset and follows up with regression and classification analytics deploying several popular machine learning algorithms.

### Project Files
The following project files are located in this project directory:

[README.md](https://github.com/hbhasin/Capstone-Project-1/blob/master/README.md) -- This document, with project description.

[Denver 2016 Bike Share Capstone Project Proposal](https://github.com/hbhasin/Capstone-Project-1/blob/master/Denver%202016%20Bike%20Share%20Capstone%20Project%20Proposal.pdf) - Project Proposal.

[Denver 2016 Bike Share Data Exploration.pdf](https://github.com/hbhasin/Capstone-Project-1/blob/master/Denver%202016%20Bike%20Share%20Data%20Exploration.pdf) - Final Project Report.

[Denver 2016 B-cycle](https://github.com/hbhasin/Capstone-Project-1/blob/master/Denver%202016%20B-cycle.pdf) - Slide Deck.

[Denver_2016_Excel_to_CSV_File_Conversion](https://github.com/hbhasin/Capstone-Project-1/blob/master/Denver_2016_Excel_to_CSV_File_Conversion.ipynb) -- Converts the Trips dataset Excel spreadsheet from a hefty 27MB file size to a reasonable 6MB compressed file.

[Denver_Bike_Share_Distance_Duration_Submit](https://github.com/hbhasin/Capstone-Project-1/blob/master/Denver_Bike_Share_Distance_Duration_Submit.py) - Used to retrieve distances between checkout and return kiosks from [Google Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/).

[Denver 2016 Bike Share Weather Data Consolidation](https://github.com/hbhasin/Capstone-Project-1/blob/master/Denver%202016%20Bike%20Share%20Weather%20Data%20Consolidation.ipynb) - Used to retrieve weather attributes from [Dark Sky API](https://darksky.net/dev/).

[Denver 2016 Bike Share - Data Wrangling](https://github.com/hbhasin/Capstone-Project-1/blob/master/Denver%202016%20Bike%20Share%20-%20Data%20Wrangling.ipynb) - Data Wrangling Notebook.

[Denver 2016 Bike Share Regression Modeling](https://github.com/hbhasin/Capstone-Project-1/blob/master/Denver%202016%20Bike%20Share%20Regression%20Modeling.ipynb) - Regression Modeling Notebook.

[Denver 2016 Bike Share Multi-Class Classification Modeling](https://github.com/hbhasin/Capstone-Project-1/blob/master/Denver%202016%20Bike%20Share%20Multi-Class%20Classification%20Modeling.ipynb) - Multi-Class Classification Modeling Notebook.

[./data](https://github.com/hbhasin/Capstone-Project-1/tree/master/data) - Folder containing data files used in the Python notebooks.

[./figures](https://github.com/hbhasin/Capstone-Project-1/tree/master/figures) - Folder containing figures used in the Python notebooks.


### Data Sources
[Denver B-cycle](https://www.denverbcycle.com/company) - The Trips dataset is located under [Denver B-cycle Trip Data](http://denver.bcycle.com/docs/librariesprovider34/default-document-library/2016denverbcycletripdata_public.xlsx?sfvrsn=2). The Kiosk dataset is located under [Denver B-Cycle Station Location Data](https://denver.bcycle.com/docs/librariesprovider34/default-document-library/october2016_kioskinfo.xlsx?sfvrsn=2).

Distances between Checkout and Return Kiosks: Distances were retrieved from [Google Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/).

Weather Data: Retrieved [Dark Sky API](https://darksky.net/dev/).

Geo-spatial Mapping: [Tableau](https://public.tableau.com/) was used to map the number of bike checkouts and returns by kiosks.

### Analysis Software
All data analyses were done in Python and publicly available libraries using Jupyter Notebook except for the geo-spatial mapping of the number of bike checkouts and returns by kiosks which was done using Tableau.

### Acknowlegements
The original plan was to use the Denver 2015 Trips dataset to continue the work by [Tyler Byers](https://github.com/tybyers/denver_bcycle). Fortunately, the 2016 dataset became available just in time for this project's undertaking. While there are certainly some differences between how the data were analyzed and reported by Denver B-Cycle and the author, credit must go to Denver B-Cycle for publishing its 2016 annual report and posting the 2016 dataset for public consumption and for use in this project in a timely and professional manner.
