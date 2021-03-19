"""

MACS 30122: Final Project - Record Linkage

"""

import pandas as pd
import os

all_json_state_names = ["Alaska", "Alabama", "Arkansas", "Arizona", 
            "California", "Colorado", "Connecticut", "DC", 
            "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", 
            "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", 
            "Louisiana", "Massachussetts","Maryland", "Maine", "Michigan", 
            "Minnesota", "Missouri", "Mississippi", "Montana", "Nevada",
            "North Carolina", "North Dakota", "Nebraska", "New Hampshire",
             "New Jersey", "New Mexico", "New York", "Rhode Island",
            "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", 
             "South Carolina", "South Dakota", "Tennessee", 
            "Texas", "Utah", "Virginia", "Vermont", 
            "Washington", "Wisconsin", "West Virginia", "Wyoming"]


def remove_u2069(t):
    '''
    Remove the Unicode character pop directional isolate (\u2069) from data
    crawled from the website.

    Input (str):
        a tweet, possible with in-line pop directional isolate
    character

    Output (str):
        a tweet, removed possible in-line pop directional
    isolate character
    '''
    return repr(t).replace('\\u2069','').replace('"','').replace("'","")


def timestamp_to_str(t):
    '''
    Alter the format of dates from timestamp to string.
    Input (timestamp):
        date in the format of timestamp

    Output (str):
        date in the format of string   
    '''
    return t.date().strftime('%Y/%m/%d')


def read_in_one_governor_tweets(input_path, file_to_link):
    '''
    Read in and construct a dataframe for tweets from one state governor.

    Input:
        input_path (str): the path of the JSON file containing tweets
        from one state governor
        file_to_link (str): the name of the JSON file (with the suffix
        of ".json")

    Output (dataframe):
        a dataframe containing tweets from one state governor
    '''
    p = input_path
    state_name = file_to_link.replace(".json","")
        
    # Read in the governors' Twitter data
    tweets_df = pd.read_json(os.path.join(p, file_to_link),lines=True,encoding='utf-8')
    tweets_df.loc[:, 'date'] = tweets_df.loc[:, 'date'].apply(timestamp_to_str)
    tweets_df = tweets_df[['tweet','date']]
    tweets_df.drop_duplicates(keep='first',inplace=True)
    tweets_df.reset_index(drop=True, inplace=True)
    tweets_df.loc[:,'province_state'] = state_name
    tweets_df['tweet'] = tweets_df['tweet'].apply(remove_u2069)
    tweets_df.rename(columns={'tweet': 'governor_tweet'}, inplace=True)

    return tweets_df


def replace_separator(t):
    '''
    Replace the separator of date format for merging.

    Input (str):
        Date in format yyyy-mm-dd

    Output (str):
        Date in format yyyy/mm/dd
    '''
    t_rep = t.replace("-","/")
    return t_rep