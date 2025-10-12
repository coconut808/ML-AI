# WEEK 5 ASSIGNMENT - Report and Findings
**Objective**: Highlight the differences between customers who did and did not accept the coupons.  

### Findings:
* There was an age value of "below21" which we set to 20, so that we can plot and compare appropriately.  The only relative significance would be when we examine which age groups used the Bar coupon.  The below21 age group should not have any usage of using the coupons at the bar. 
* We converted the age value of '50plus' to '50' to keep integer values.
* The 'passenger' column was spelled incorrectly so it was renamed from 'passanger' to 'passenger'.

**Hypothesis:**  Why would the type of car matter on whether a coupon is/was accepted or not?
* After examining the data, the conclusion is that it did not matter.  Only .85%, less than 1%, of records provided a value for car data. This column was dropped for the rest of the analysis.  

**Hypothesis:** Does eduction have an impact on whether a coupon is used.  My theory was it did not.  I would think that folks in the higher eduction (some gollege or higher) would be less likely to use coupons because it was unplanned costs and would not be saving money.  However, quite the opposite is true.  Higher eduction levels correlate with higher coupon usage.  

**Hypothesis:** Following up on our assumption earlir implied that any person(s) under the 21 would not be using the coupons at the bar.  To my surprise there were 36 people below 21 who used a coupon at the bar. 


**Proprtion of total observations:**
* 56.84% of the total observations chose to accept the coupons.
* 'Coffee house' was the most popular type of coupon accepted as depicted by the plot below. 
![coupon distribution](images/coupon_distribution.png)
