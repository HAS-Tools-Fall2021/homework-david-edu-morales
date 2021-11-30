# David Morales, 11/28/21, HW14

## Discussion

____
## Grade
3/3: Great job!  I'm sorry you weren't able to get it running but I think your experience is representative of what a lot of research codes look like. Its a good example of how much work it takes to actually make somethign usable for others. 
____

### 1. Paper information:
   - Title: Hot extremes have become drier in the United States Southwest
   - Link: https://www.nature.com/articles/s41558-021-01076-9
   - Summary: This paper looks to understand how specific humidity will change in climatologically dry regions as a result of anthropogenic climate change. The impacts of summer heat are mediated by humidity, however this paper shows that in low-humidity regions, decreases in humidity co-occur with increases of hot temperature extremes in the Southwest.

### 2. Code information:
   - Code access: https://github.com/karenamckinnon/compound_extremes
   - Data access: https://www.ncei.noaa.gov/data/global-hourly/access/
   - Summary: The paper included a link to Dr. Karen McKinnon's GitHub repos including the primary repo 'compound_extremes.' Furthermore, according to the README.rst contained in 'compound_extremes,' I was instructed to download two packages on McKinnon's GitHub, 'helpful_utilities' and 'humidity_variability.' Unfortunately, these weren't actual Packages, but separate repos on McKinnon's GitHub that I cloned.  

### 3. Experience summary:
   - The README.rst used GitBash/Terminal codes to download the data, fit the model, and run that scripts. Unfortunately, I never made it past the first phase of downloading the data. According to McKinnon's readme, "Code is research (not production) quality, and will likely need modifications to run on your machine." There were several locations in the scripts where lines of code were commented out but there were no explicit instructions regarding if these lines were necessary or needed to be edited.
   - The organization was also convoluted. An instruction reading, "Note that you will need to install the Climate Data Store API, and set up authentication" occurred late in the 'compound_extremes' README.rst and did not provide guidance on how to install or set up authentication for this.
   - As for the documentation within the code, it was well commented at some places and missing at other places.

### 4. Running the repo:
   - As mentioned above, I was not successful in running the code. Perhaps the most important step, accessing the data, was poorly commented and instructions were not given on what to change to make the code usable on my machine. Thus, I'm not sure how easy it would have been to run the analytics script.

### 5. Data access:
   - The data did not have a DOI. In fact, there was a special script in the repo dedicated to accessing the data from NOAA's Integrated Surface Database. This script had no comments regarding usability, just comments regarding what some parts of the code was responsible for. I was able to see that the data was to be access via an API and imported into a csv file that would be created on my computer.

### 6. Reflection:
   - This experience was very illuminating. I feel as though a lot of my code focuses on declarative statements about what portions of code do instead of using informative statements that tell the user how to interact with the code. Of course, I recognize that my code thus far has not been complex enough to warrant extensive use of informative comments. For the author, I would suggest they spend more time understanding how different computers/users can access the data and providing adequate instructions for other users. 