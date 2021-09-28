# David Morales, 09/26/2021, HW5

____
## Grade
3/3: Grerat work!  I like what you were doing isolating the late september early octobe parts. FYI you don't need to go into a list to merge them thoug you can just do that dirctly from your dataframes. Also I dont think it will be good to set year as the index because this is not going to be unique for every entry. Feel free to come by my office hoursr if you want to go over this more. 

## Rationale:
I started this exercise exploring how I could isolate the 7-day week across years so that I could take the average flow. It was difficult understanding how I could isolate the relevant September and October dates in a single line of code; it's still unclear to me how to filter for rows that satisfy multiple double conditions in a single line of code (e.g., month == 9 & day >= 27 AND month == 10 & day <= 3).

If lieu of that: I first reindexed the rows to their corresponding years; isolated the Sept. and Oct. rows into two separate lists; filtered out for relevant dates in each list; concatenated the two lists into one; grouped by year and found the average value for each year.

I found that looking at the grand average of yearly averages since 2010 and 2015 came to 110cfs. I then used the .describe() method of the 7-day average by year dataframe and saw that years with higher averages tended to have larger standard deviations. Values closer to 110 tended to have tighter std values so I felt confident that my prediction wouldn't be subject to large amounts of variability.

## Questions:
1. *Provide a summary of the data frames properties:*

| #  | Column    | Non-Null Count | Dtype  |
|--- | ------    | -------------- |-----   |
| 0  | agency_cd | 11954 non-null |object  |
| 1  | site_no   | 11954 non-null | int64  |
| 2  | datetime  | 11954 non-null | object |
| 3  | flow      | 11954 non-null | float64|
| 4  | code      | 11954 non-null | object |
| 5  | year      | 11954 non-null | int32  |
| 6  | month     |11954 non-null  |int32   |
| 7  | day       |11954 non-null  |int32   |

- *What are the column names?* 
  - see "Column"
- *What is its index?*
  - see "#" column
- *What data types do each of the columns have?*
  - see "Dtype" column

2. *Provide a summary of the flow column including the min, mean, max, standard deviation and quartiles.*
   
|Stat   |Value         |   
|-------|--------------|   
|count  |  11954.000000|
|mean   |    340.923289|
|std    |   1391.281051|
|min    |     19.000000|
|25%    |     93.500000|
|50%    |    157.000000|
|75%    |    214.000000|
|max    |  63400.000000|

3. *Provide the same information but on a monthly basis. (Note: you should be able to do this with one or two lines of code)*
	flow

|month|count|mean	    |std	        |min	|25%        |50%	|75%	|max	|
|---|-------|-----------|---------------|-------|-----------|-------|-------|-------|
|1	|1023.0	|691.002933	|2708.527013	|158.0	|201.000	|218.0	|285.00	|63400.0|
|2	|932.0	|903.156652	|3300.470852	|136.0	|200.000	|238.0	|615.75	|61000.0|
|3	|1023.0	|919.477028	|1625.606804	|97.0	|178.000	|368.0	|1045.00|30500.0|
|4	|990.0	|295.596970	|540.712365	    |64.9	|111.250	|140.0	|210.00	|4690.0|
|5	|1023.0	|104.410850	|50.394386	    |46.0	|77.050	    |92.0	|117.50	|546.0|
|6	|990.0	|65.534949	|28.660493	    |22.1	|48.925	    |60.0	|76.55	|481.0|
|7	|1023.0	|108.447312	|219.942070	    |19.0	|53.500	    |71.0	|112.50	|5270.0|
|8	|1023.0	|171.500782	|295.999467	    |29.6	|77.950	    |116.0	|178.00	|5360.0|
|9	|983.0	|170.977009	|283.050814	    |37.5	|88.550	    |119.0	|169.50	|5590.0|
|10	|992.0	|144.094556	|110.663378	    |59.8	|104.750	|124.0	|152.25	|1910.0|
|11	|960.0	|203.198958	|232.211365	    |117.0	|154.000	|174.0	|198.00	|4600.0|
|12	|992.0	|331.986895	|1080.358791	|155.0	|190.000	|203.0	|226.00	|28700.0|

4. *Provide a table with the 5 highest and 5 lowest flow values for the period of record. Include the date, month and flow values in your summary.*
   
|	 |datetime    |    flow|
|----|------------|--------|
|1|	1993-01-08|	63400.0|
|2|	1993-02-20|	61000.0|
|3|	1995-02-15|	45500.0|
|4|	2005-02-12|	35600.0|
|5|	1995-03-06|	30500.0|
|11950|	2012-07-03|	23.4|
|11951|	2012-06-29|	22.5|
|11952|	2012-06-30|	22.1|
|11953|	2012-07-02|	20.1|
|11954|	2012-07-01|	19.0|

5.  Find the highest and lowest flow values for every month of the year (i.e. you will find 12 maxes and 12 mins) and report back what year these occurred in.
- Please run **code line 54** for complete list of month max/min from 1989-2020

6. *Provide a list of historical dates with flows that are within 10% of your week 1 forecast value. If there are none than increase the %10 window until you have at least one other value and report the date and the new window you used*
- Please run **code lines 56-63** for complete list of dates that fell between 10% higher or lower of 110cfs prediction. 