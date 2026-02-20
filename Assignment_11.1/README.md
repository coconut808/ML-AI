# Executive Summary

## Problem Statement: 
Help used car dealers interested in fine-tuning their inventory

## Data Description:
The dataset contains information on used car.  Source: Kaggle

## EDA



## Analysis


* Supplmental Analysis on Luxury/Exotic cars provided below. 




### Supplemental - Luxury/Exotic Cars
These vehicles were typically higher in price which skewed the data on pricing.  Due to the higher cost of the vehicle, the operating costs (storing, securing, insurance, maintenance, parts) would cost more for dealerships.  Typically these vehicles can be found at used dealerships that specialize in luxury/exotic cars.  As one may expect, this would also attact a different segment of customers as well. 

Data points to highlight:
* They all have a clean title. 
* Topping the list of the manufacturers are mercedes-benz, ferrari, and porsche. 
* There are less older exotic vehicles.  Any oler models these are generally rare and may be considered collectables.
* No exotic/luxury cars with odometer readings over 250,000 miles in our dataset.  With the highest topping out at 217,000 miles.
* There are some records with mileage under 50 miles which would be classified as new. Which also eliminates them from the used car dataset. 
* Transmission in these higher price range cars have a higher percentage (84.3%) with a classifcation of excellent, like new, good. 
* Most of the transmisison is automatic.












There are 2 files here currently: 
* eda.ipynb - jupyter notebook used during exploratory data analysis
* luxury.ipynb - jupyter notebook fun EDA on luxury/exotic cars 
* prompt_ii.ipynb - main notebook with business reasoning and cases

Some initial analysis shows that the number or cars start to tail of in the 1990s so we're going to use data between 1995 and 2024 which is about 30 years of data. The median price did not change much going from a 50 year window to a 30 year window. 

Median price from 1975-2024
![year_price_1975_2024](images/cleaned_year_price_1975_2024.png)
Median price from 1995-2024
![year_price_1995_2024](images/cleaned_year__price_1995_2024.png)

*Car color* 
* Interestingly, white, black, and silver are the top color choices for cars.  Same holds true for luxury/exotic cars.





























----

# Supplemental
Some data plots created in EDA, pre data cleaning: 
![dirty_year_price](images/dirty_year_price.png)
![cleaned_year_price_1975_2024](images/cleaned_year_price_1975_2024.png)




