# Record linkage

#The aim of this .py file is to link Covid data (a csv file under the "data" folder) to Twitter data.
#The function can both link Covid data to raw Twitter data (in json) or preprocessed data (in csv).


import pandas as pd
import os


def timestamp_to_str(t):
    return t.date().strftime('%Y-%m-%d')


def record_linkage(input_path, file_to_link):
        '''
        The constructor for the RecLink class. Loads data files for processing and
        fills in missing values to prevent DataFrame operation errors.
        Parameters:
            None
        Returns:
            (RecLink): a new instance of the class
        '''
        p = input_path
        
        # Read in the Twitter data, can accept .json or .csv file
        if "json" in file_to_link:
            tweets_df = pd.read_json(os.path.join(p, file_to_link),lines=True)
            tweets_df.loc[:, 'date'] = tweets_df.loc[:, 'date'].apply(timestamp_to_str)
        elif "csv" in file_to_link:
            tweets_df = pd.read_csv(os.path.join(p, file_to_link))
            
        # Read in the Covid data
        covid_data_by_country = pd.read_csv(os.path.join(p, "covid-data-by-country.csv"))
        
        merged_df = pd.merge(left = tweets_df,right = covid_data_by_country, on = 'date')
        merged_df.reset_index(drop=True, inplace=True)
        return merged_df

