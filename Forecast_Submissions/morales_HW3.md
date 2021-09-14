# David Morales, 09/10/21, HW3
___
### Grade
3/3: Great work! I like your approach for your forecast.  
- Picking statistically relevant years is a huge challenge especially in systems that are changing.
- Check out the solution key for this assignment to see how I solved the questions if you are looking for other ways to write things with less lines. We will start working on this more as we get a little more under our belts.  
_____

## Rationale:
I thought it would best to look at the average weekly flows from the same span of days (13-19 and 20-26) across all September months recorded from 1989 to 2020. Taking these two averages, I felt it would be the best to base my two predictions on these values.
- I did consider searching for past summers with similar flow rates to this year's and basing my predictions on the corresponding September flow rates but I was having trouble coherently searching for matches to this year. I think I'm also lacking a firm understanding of how to identify statistically relevant data (i.e., if I found a year with similar flow rate to this year's, could I be confident that it's September flow would be predictive of this years?).
- I'm wondering, in future iterations, how I could pare down my code. I think as I develop a better grasp on list comprehensions and for loops, I'll be able to write in accordance to the DRY principle.

## Questions:
1. Flow, year, month, and day are all lists that have pulled data from the streamflow_week3.txt file we downloaded from the USGS website.
   - Each list contains the information specific data from each row in the text file (e.g., Flow is a list that contains the daily flow averages of every day since 1989).
   - The flow list contains float type data while year, month, and day are all integer data types.
   - Each list contains 11,939 values.
2. For Forecasted Week 1, my estimation is an average flow of 159cfs. Since 1989, there have been 289 daily flow averages that exceed my prediction (29.86% of measured Sept. flows). For Forecasted Week 2, my estimation is an average flow of 194cfs. Since 1989, there have been 179 daily flow averages that exceed my prediction (18.49% of measured Sept. flows).
3. Shifting comparison data relative to Forecasted Week 1 value(159cfs):
   - Pre-2000: Daily flow avg. in Sept. greater 132 times (40%)
   - Year 2000: Daily flow avg. in Sept. greater 2 times (6.67%)
   - Year 2010: Daily flow avg. in Sept. greater 0 times (0%)
   - Since 2010: Daily flow avg. in Sept. greater 72 times (23%)
4. Daily flow average of the first half of Sept. since 1989 is 177.71cfs as compared to a daily flow average for the second half of Sept. since 1989 of 166.42cfs. Thus, the daily flow decreases from the first half of Sept. to the second half. Despite that, my predictions are actually increasing from a one-week prediction to my two-week prediction.
