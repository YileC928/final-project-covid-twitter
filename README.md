# MACS30122 Final Project - COVID-19 Data and CDC's Tweets Analysis

final-project-covid-twitter created by GitHub Classroom

**This repository is for final project for course MACS 30122.**

**Team name**: covid-twitter

**Team member**: Jinfei Zhu, Xi Cheng, Boya Fu, Yile Chen

**GitHub Repository**: https://github.com/cs-ssa-w21/final-project-covid-twitter

**Goals**: 2020 is all about Covid-19. This unprecedented global pandemic has changed everyone's daily normal and we are willing to find out what CDC news relates to the change of the number of covid infected persons and death. In the meantime, in the United States, many governors like Andrew Cuomo of New York State will give covid administration on Twitter. We would also collect data from several states seriously influenced by Covid. If time permits, we would collect data from all states' governors. We would build a web interaction page (probably using flask) that when users input a time period and state name, they can see the covid number and CDC & governors policy guidelines and covid-related policies.

Our analysis contains five parts:
- Data Collection (Jinfei Zhu)
- COVID Data Analysis (Jinfei Zhu)
- CDC Tweets Content Analysis (Xi Cheng)
- Record Linkage (Boya Fu)
- User Interface to input `date` or `state name` and output CDC Tweets on that date and COVID numbers (Yile Chen, Boya Fu)

# Prerequisites

Following packages needs to be downloaded to successfully run this notebook:

[Plotly (version 4.14.3)](https://pypi.org/project/plotly/)

`pip install plotly`

[nbformat 5.1.2 (version 5.1.2)](https://pypi.org/project/nbformat/) 

`pip install nbformat`


# Data Source:

## Twitter: 

CDC: https://twitter.com/CDCgov


Governors' Tweets: 

We have collected Twitter from 51 governor's Twitter. Their handle are in `data\governor-twitter-handle.csv`. Here are some examples:

Illinois Governor JB Pritzker: https://twitter.com/GovPritzker

New York Governor Andrew Cuomo: https://twitter.com/NYGovCuomo

## Covid Data: 

JHU COVID MAP: https://coronavirus.jhu.edu/map.html

# Files in this repository

## Main repository
`[Final Output] COVID-19 Data and CDC's Tweets Analysis.ipynb `: The main output Jupyter Notebook.

`scrape_twitter_with_Twint.py`: Python functions to scrape twitter with Twint.

`covid_data_analysis.py`: Python functions to do COVID data cleaning, analysis, and visualization.

## Code:

`covid-big-query-by-country.sql` and `covid-big-query-by-state.sql`: SQL scripts to retrieve COVID data from Google Bigquery platform

`data\governor-twitter-handle.csv`: Specific Twitter handles for each governor

## Data:

`cdc_twitter_covid.json`: All CDC Tweets that mention the term 'COVID'

`cdc_twitter_since_2020.json`: All CDC Tweets from 2020-01-01 to 2021-02-22

`State` folder: This folder contains 51 json files documenting all Tweets that mention the term 'COVID' in each governor's Twitter

`covid-data-by-state.csv`: COVID data by states from 2020-01-01 to 2021-02-22, including confirmed and deathes

`covid-data-US.csv`: COVID data of the US from 2020-01-01 to 2021-02-22, including confirmed and deathes



# References:

## Data Collection

*Twint Package*

Pacage Introduction: 

    https://github.com/twintproject/twint
    
Configuration Options: 

    https://github.com/twintproject/twint/wiki/Configuration

*Other information*

Debugging: 

    https://github.com/twintproject/twint/issues/1121#issuecomment-773521415
    
Combine json files into one json: 

    https://www.freecodecamp.org/news/
    how-to-combine-multiple-csv-files-with-8-lines-of-code-265183e0854/

## COVID Data Analysis

Regex in pandas: 

    https://kanoki.org/2019/11/12/how-to-use-regex-in-pandas/
    
Seaborn: 

    https://seaborn.pydata.org/generated/seaborn.FacetGrid.html
    
    https://seaborn.pydata.org/generated/seaborn.relplot.html
    
plotly: 

    https://plotly.com/python/choropleth-maps/
    
Constructing a python package with different files:

    https://python-102.readthedocs.io/en/latest/packaging.html
    
ARIMA:

    https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-forecasting-with-arima-in-python-3
    
    https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_model.ARIMA.fit.html

COVID Prediction:
    
    https://towardsdatascience.com/model-the-covid-19-epidemic-in-detail-with-python-98f0d13f3a0e
 
    
## Tweets Analysis

Tweet preprocessing: 

    https://pypi.org/project/tweet-preprocessor/

