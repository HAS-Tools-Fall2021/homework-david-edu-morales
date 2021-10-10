# Instructions for HW7 Partner Assignment:

## Intro:
Hello. I tried to make the script and these instructions as straightfoward as I could; honestly, it's as simple as running each cell sequentially. I wasn't sure what I was supposed to set up for you, nor did I understand if--and to what degree--you were supposed to interact with the code.

Enjoy!

## Summary:
This script begins with:
- Package Import

Which is followed by:
- Filepath creation
- Data read-in
- Datetime parsing for ease-of-use

Then, I establish four (4) functions:
- historical_flow() : finds historical mean flow of set timeframe
- add_dQ_df() : calculates and adds change in flow (dQ)
- flow_analysis() : generates plots of mean flows & dQ
- week_stat() : generates and prints stats of mean flow dataframes

Finally, the script that creates the objects you will interact with via the above created functions. *Again, you simply need to run each cell in order, that's it.*

**Note: My weekly forecasts are found at the bottom of the print output from line252-258**

I hope this helps.

Take care,

David

Forecast Values:

Week 1 forecast: 130.48

Week 2 forecast: 124.23

Plots:
[Mean flow by year](../data/yearly_means.png)

[Change in mean by year](../data/yearly_delta.png)

[Scatter plot of yearly mean change](../data/delta_scatter.png)

[Mean flow by year for 10/11 to 10/17](../data/yearly_mean_wk1.png)

[Change in mean by year for 10/11 to 10/17](../data/yearly_delta_wk1.png)

[Scatter plot of yearly mean change for 10/11 to 10/17](../data/delta_scatter_wk1.png)

[Mean flow by year for 10/18 to 10/24](../data/yearly_mean_wk2.png)

[Change in mean by year for 10/18 to 10/24](../data/yearly_delta_wk2.png)

[Scatter plot of yearly mean change for 10/18 to 10/24](../data/delta_scatter_wk2.png)

Code Review:
Easiness of script to understand: 2/3.  First function is written very well, describes in detail the process being done, along with the input and output parameters.  Other functions describe parameters well, but could be more descriptive with the processes involved.  Comments are decent, could give a bit more detail.  Script itself was very easy to run on my own, and doc strings and variable names were useful and descriptive.

Pep8 Format: 3/3.  Very good formatting, no warnings or errors after turning on the linter.

Code efficiency: 2.5/3.  A lot is being done by this code, but it manages to do everything in an efficient manner.  Functions are prompt, expedite the running of code, and statements and operations are kept to one line if possible.  The code remains readable throughout, but there is a minor error in the final print statement: the forecast values are supposed to be rounded, but this rounding is not done until after the print statement.  Other than that, though, the code is easily understood an runs efficiently.
