# Big-Data-Soccer-Analytics
CS594-BigData-Project
# Big-Data-Soccer-Analytics-twitter-recipe
==========================
### Version
1.0.0

Welcome to the Soccer Data Analysis recipe!

**Brief Description:**
- Data Acquisition:
	- Connect to Twitter API
	- Fetch tweets based on preset keywords
	- Format the data received
- Data Storage:
	- Dump acquired data to MongoDB database
- Data Analysis:
	- Run sentiment analysis on historical data from the database
	- Run sentiment analysis on live tweets
	- Run statistical analysis on the data from the database
- Visualization:
	- Plot histogram to show top 10 countries in terms of soccer popularity
	- Generate Kernel density graph on historical data
	- Generate raw sentiment analysis graph on historical data
	- Generate twitter sentiment volume graph on historical data
	- Generate Kernel density graph on live tweets
	- Generate raw sentiment analysis graph on live tweets
	- Generate twitter sentiment volume graph on live tweets
	- Generate dynamic world map to display continent wise soccer popularity  

#### Related Links ####
- For more information on AlchemyAPI's sentiment analysis API: http://www.alchemyapi.com/products/features/sentiment-analysis/
- For more information on Twitter's API: https://dev.twitter.com/rest/public
- For more information on MongoDB: http://www.mongodb.org/
- For more information on R: http://www.r-project.org/
- For more information on worldmap: http://www.fusioncharts.com/
- For more information on setting up the web Server: https://www.apachefriends.org/index.html
- For more information on the web app: http://php.net/

## Requirements ##
- An API key from AlchemyAPI -- register for one at: http://www.alchemyapi.com/api/register.html
- Credentials for Twitter API -- the Consumer Key and Consumer Secret (create a new application at: https://dev.twitter.com/apps)
- An installation of MongoDB -- http://www.mongodb.org/downloads
- An installation of R, and the "ggplot2" package -- see e.g., http://cran.cnr.berkeley.edu/ and http://www.r-bloggers.com/installing-r-packages/
- Python pymongo for MongoDB connections
- Python tweepy to connect to tweeter API
- FusionCharts for creating the world map
- php for setting up the web app
- Xampp for setting up the web server

## STEP 1: Gather/format the data and insert it into the mongoDB instance ##
This process is completely handled by the script datadump.py. In the UI console this script can be accessed by
clicking the link: "Feed database with live tweets".

## STEP 2: Run analysis on the gathered data ##
- This process is handled by:
`alchemyapi\recipe.py` This takes care of the static sentiment analysis on the historical data from the database. This can be invoked
through the: "Run Past Tweet Analysis from MongoDB" link in the web app.
- ```bash dyn\recipe.py``` This takes care of the dynamic tweets sentiment analysis. This can be invoked through the: "Run Current Tweet Analysis by fetching tweets" link in the web app.
- ```bashcountry-count.py``` This generates the statistical data points on the data in mongoDB.

## STEP 3: Visualize the data##
-  **Run Analysis Live Streaming on Data(Dynamic Data)**
	- This process is handled by:
	```bash $> alchemyapi\recipe.py```
	This takes care of the dynamic sentiment analysis on the data coming from twitter data streaming through twitter api called 'tweepy'.
	'R'Framework\ggplot library-This takes care of the graphs generated on the data generated from recipe.py. To do this, simply invoke the included R script as follows:
        ```bash R < plot.R --vanilla ```
        
        
	- 3 types of graphs are generated. 
   		- 1) Kernel density graph.
   		
   		- 2) Twitter Volume graph
   		- 3) Hourly Sentiment Analysis graph.


       		- **Graph description:**
	Sentiment Anaysis per hour graph: a histogram showing the positive and negative Tweet scores
	Kernel density graph: a kernel density function corresponding to the above histograms
	Twitter Volume graph: a plot showing Tweet volume (separated by sentiment) as a function of the hour in a day
	Dependencies:
	You must have R installed on your system to run this tool.
	You must also install the 'ggplot2' library for R
	Delete your data:
From time to time, it's good to empty out your cache! If you want to wipe the twitter_db instance in MongoDB that was created in STEP 1, run the command as follows :-
python delete.py



- **Top 10 countries with Mean:**
    - This process is handled by:
```bash $> new_Country_Count.py``` - This script will plot the bar graph. We are showing the tweets of top 10 countries where soccer is most popular compared to the rest of the world.
For calculating this we have taken help of in built python functions like map as well as utilized external libraries like pandas and matplotlib for plotting the graph.
We are collecting the count of tweets country wise and after getting the count we are calculating the mean of tweets and we also have plotted the mean on the graph.

	- Types of graph generated: Bar graph with mean value
	- Requirements: You must have installed pandas, matplotlib, numpy, json packages.

- **Statistics Update Script:**
	- In this step we will show the statistical analysis of our data.
It will show the mean, median, standard deviation and the mode values of tweets.

- **Worldmap Dashboard:**
	- This process is handled by:
```bash $> dashboard.py``` - This script will take country wise count of tweets  and after mapping country code to their respective continents code it will finally count continents wise total number of tweets.
At last it will store data in a json file jsonData.json.
new-dashboard.html - Html file is used to show dashboard.
```bash $> ReplaceWords.py``` 
 

	- This script will use data from jsonData.json file and update new-dashboard.html file and generate updated_dashboard.html.
updated_dashboard.html - This file will show the worldmap dashboard.
	- Dashboard description: Fusioncharts garph has been used to show the worldmap dashboard.
					   It will show the total number of tweets continents wise.
					   
- **PHP Dashboard:**
    - The php console will handle the entire project and can be used to generate reports automatically. It also hosts all the scripts required to acquire and store data and can be used to start the respective scripts to execute their functionality.


