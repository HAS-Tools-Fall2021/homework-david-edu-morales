# Week 6: Python skills week 4<!-- omit in toc -->
This week we are going to continue using Pandas DataFrames and we will be focusing on plotting with matplotlib.
____
## Table of Contents:<!-- omit in toc -->
- [To Do List](#to-do-list)
- [References](#references)
- [Required Training Activities](#required-training-activities)
- [Assignment 6: Matplotlib](#assignment-6-matplotlib)
  - [Forecast Rules for this week:](#forecast-rules-for-this-week)
  - [What to submit:](#what-to-submit)
  - [Assignment](#assignment)
___
## To Do List
1. Complete the required training Activities by **next Tuesday**, get through as much as you can before class **this Thursday**.
2. Submit your sixt streamflow forecast and assignment by **noon on Monday** following the instructions in the [ Forecast Assignment](#assignment).
3. Note that our next cheat sheet will be on Numpy and this will be do **next Thursday**

___
## References
- There are two images in the Cheet_sheets folder that covers the major plotting commands: `matlotlib_commands.png` and `matlotlib_commands2.png`

- You should also check out the [matplotlib website](https://matplotlib.org/) I especially recommend the [plot gallery](https://matplotlib.org/gallery/index.html) as a good place to get started.

- [Python Data Science Handbook Chapter 4](https://jakevdp.github.io/PythonDataScienceHandbook/) (sections of this chapter are also assigned in the required training).
___
## Required Training Activities
1.  Read the following sections from the [Python Data Science Handbook Chapter 4](ttps://jakevdp.github.io/PythonDataScienceHandbook/index.html). Note that this material is more detailed than the Earth Data Science Handbook. Its fine if you don't have time to work through every example they discuss but at a minimum you should read through these sections to be familiar with the concepts and know where to refer back to as needed:
  - [Simple Line Plots](https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html)
  - [Simple Scatter Plots](https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html)
  - [Visualizing  Errors](https://jakevdp.github.io/PythonDataScienceHandbook/04.03-errorbars.html)
  - [Histograms, Binning and Density](https://jakevdp.github.io/PythonDataScienceHandbook/04.05-histograms-and-binnings.html)
  - [Customizing  Plot Legends](https://jakevdp.github.io/PythonDataScienceHandbook/04.06-customizing-legends.html)
  - [Customizing Colorbars](https://jakevdp.github.io/PythonDataScienceHandbook/04.07-customizing-colorbars.html)
  - [Multiple Subplots](https://jakevdp.github.io/PythonDataScienceHandbook/04.08-multiple-subplots.html)
  - [Customizing  Matplotlib: Configurations and Stylesheets](https://jakevdp.github.io/PythonDataScienceHandbook/04.10-customizing-ticks.html)
___
## Assignment 6: Matplotlib
This week we will be using plots to help us make better forecasts

(*Remember* you should copy the starter code into your own repo and not work with it directly on the course materials repo).

### Forecast Rules for this week:
- You must use the pandas dataframe *data* created at the top of the starter code as the basis for your analysis.

- You can do any mathematical operation you would like on the dataset as long as you only use the numpy or pandas package to do so.  

- The only dataset you can use is the historical observed streamflow (Station 09506000 Verde River Near Camp Verde, refer to previous weeks for download instructions if needed. )

- You can use the streamflow data up to the Saturday before the forecast is due for making your decisions.

### What to submit:
This week you should submit the following (for more details on submitting through GitHub refer to previous weeks instructions):

1. Your streamflow forecast values in the forecast repo in the csv with your name

2. Your assignment summary (see instructions below). This should be named with the same convention  as always `lastname_HWx.md` and saved in the submission folder of your homework repo.  It should include
  - An appropriate header 
  - Appropriate markdown formatting to make it easy to read
  - Answers to all of the questions listed below

3. The python script you wrote to do your homework.  Just copy this script into the submission folder with the name `lastname_HWx.py`. 
  
**NOTE1:** *Even if you have a free pass on the written assignment for this week you should still build AR models and graphs and submit your python script.*

**NOTE2:**: You need to includ plots in your markdown this week. See the instructions from last week on adding plugins for markdown image handling in VSCoe and Atom 

### Assignment
Review the starter code I have provided as well as the training materials for examples on how to create plots. You can submit whatever plotting is most helful to you for making your forecast, **the only rule** is that they **must** be something you have created (i.e. you can't submit the starter code pltos without making modificaitons).

- For your write up you should present your plots and for every plot provide a short summary of (1) how you made it, (2) why you made it and what it tells you. 

- Your submission should include at least:
  - **6 plots total** that are your own creation. You can use the starter code plots to get you going but must have made modifications to any plot you submit (e.g. changing the data that is plotting, changing colors, line styles, legends). 
  - **3 different types of plots** (e.g. line plots, barplots, histograms, etc.) 

- See the note at the end of the previous section for how to add these into your markdown file if you are not sure how to do that

-  Finally, provide discussion of your forecast values for the week and how they were informed by your plotting
