'''
Reference: 

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

Notes: Now using Twitter Data requires a Twitter Developer Account, 
    which takes several days to get approved.
    So we use Twint package that can help us scrape Twitter data 
    without Twitter Developer Account.

'''
import os
import pandas as pd 

import twint
import nest_asyncio
nest_asyncio.apply()

def get_tweets(username=None, search=None, since=None, 
                until=None, output=None):
    '''
    Get Tweets with Twint package.
    Input:
        username(str): User of interest
        search(str): search terms
        since(str): filter Tweets sent since date 'yyyy-mm-dd'
        until(str): filter Tweets sent until date 'yyyy-mm-dd'
        output(str): the file name of the output json file
    Output:
        A json file containing tweets.
    '''
    # Configure
    c = twint.Config()
    if username:
        c.Username = username
    if search:
        c.Search = search
    if since:
        c.Since = since
    if until:
        c.Until = until
    if output:
        c.Output = output
    c.Store_json = True 

    # Run
    twint.run.Search(c)


def get_tweets_from_multiple_users(users, output, folder, search=None, 
                                since=None, until=None):
    '''
    Get Tweets from ultiple users
    Inputs:
        users(lst): a list of Twitter user names
                 like ['CDCgov', 'NYGovCuomo', 'GovPritzker']
        search(str): search terms
        since(str): filter Tweets sent since date 'yyyy-mm-dd'
        until(str): filter Tweets sent until date 'yyyy-mm-dd'
        output(str): the file name of the output json file
        folder(str): a folder name to store multiple json files
    Output:
        A json file containing all Tweets from multiple users
    '''
    # crete a list to store the output file names
    output_lst = []

    for user in users:
        user_output = r'{}\{}.json'.format(folder, user)
        output_lst.append(user_output)
        get_tweets(user, search, since, until, user_output)

    combined_df = pd.concat([pd.read_json(f) for f in output_lst])
    combined_df.to_csv(output, index=False, encoding='utf-8-sig')



        

