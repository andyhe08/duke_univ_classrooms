import requests
import csv
import json
import pandas as pd
import numpy as np

# Get list of Subjects - Run Once

sub_url = "https://streamer.oit.duke.edu/curriculum/list_of_values/fieldname/SUBJECT?access_token=" + access

sub_cont = requests.get(url = sub_url).json() # contains all information

codes = sub_cont['scc_lov_resp']['lovs']['lov']['values']['value'] # looks specifically at wanted values

toKeep = np.array([])
refined = np.array([])

for i in range(len(codes)): # Finds which subjects are taught in Durham
    if not '_' in codes[i]['code'] and not '@' in codes[i]['code']:
        toKeep = np.append(toKeep,i)

for j in toKeep: # Keeps only these subjects
    refined = np.append(refined,codes[int(j)])
        
pd.DataFrame(refined.tolist()).to_csv('subjects.csv')
