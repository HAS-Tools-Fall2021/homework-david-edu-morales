# David Morales, 09/19/21, HW4

## Rationale:
I still believe there is a lot of knowledge to be acquired looking at average values of the week that I'm estimating. I looked at all flows between 9/19-25 since 1989 and took the average; I obtained 193cfs just as I did last week. It then occurred to me that 193 was an average that didn't take years into consideration; perhaps the average value was being skewed by powerful flows from earlier years.
I tried (unsuccessfully) to write code that could output every year's average flow for the week of 9/19-25. Instead, I took another general average of the weekly flow since 2010 and came with a new average of 109cfs.
With the standard deviation function, I found that 68% of the data vary between 109 +/- 40.6. Then looking at the median value of 95.7cfs gave me the idea that I should underestimate relative to the average value of 109. 
I was able to look at the deciles for all Sept. flow since 2010; the 4th decile is at 93.08cfs. This shows me that even when the entire month is taken into account, my prediction of 95 isn't far from what is to be expected. 

## Questions:
2. *Describe variable flow_data:*
- *What is the variable flow data?* 
  - Flow data is a numpy array
- *What type of values is it composed of?*
  - The array is composed of float data elements.
- *What are its dimensions and total size?*
  - The array has 2 dimensions and its total size is 11,948 rows and 4 columns.

3. *How many times was the daily flow greater than your prediction in the month of September?*
- The daily Sept. flow was greater than 95cfs **652** times.
- **66.73%** of Sept. daily flows were greater than 95cfs. 

4. *How would your answer to the previous question change if you considered only daily flows in or before 2000?*
- Sept. daily flows before 2000 were higher than 95cfs **302** times.
- That accounts for **83.89%** of the recorded daily flows.

5. *Same question for the flows in or after the year 2010?*
- Sept. daily flows after 2010 were higher than 95cfs **202** times.
- That accounts for **58.21%** of the recorded daily flows.

6. *How does the daily flow generally change from the first half of September to the second?*
- Avg. flow of 1st half of Sept.: 176.56cfs
- Avg. flow of 2nd half of Sept.: 166.11cfs