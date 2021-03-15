import requests
import csv
import json
import pandas as pd
import numpy as np

# Get list of Course IDs - Run Once

subjects = pd.read_csv('subjects.csv')
course_ids = np.array([])

for i in range(len(subjects)): # for each subject append all the course_ids to one big numpy array
    code = subjects['code'][i]
    desc = subjects['desc'][i]
    
    spec_url = 'https://streamer.oit.duke.edu/curriculum/courses/subject/' + code + "%20-%20" + desc + "?access_token=" + access
    
    try: # SOMETIMES THE CLASS CODES DO NOT WORK, THUS THE TRY | EXCEPT 
        spec_cont = requests.get(url = spec_url).json() 
        
    except: 
        print('failed: ' + code)
        continue;
    
    num_crs = int(spec_cont["ssr_get_courses_resp"]["course_search_result"]["ssr_crs_srch_count"]) # number of offerings to search for special cases
    
    if num_crs == 0: #special case
        continue;
    
    if num_crs == 1: #special case
        spec_id = spec_cont["ssr_get_courses_resp"]["course_search_result"]["subjects"]["subject"]["course_summaries"]["course_summary"]['crse_id']
        course_ids = np.append(course_ids,spec_id) # add the specific crse_id
        continue;
    
    for j in spec_cont["ssr_get_courses_resp"]["course_search_result"]["subjects"]["subject"]["course_summaries"]["course_summary"]: # add each crse_id in the current subject
        course_ids = np.append(course_ids, j["crse_id"])

course_ids = np.unique(course_ids)

print('length: ' + str(len(course_ids))) # should be 9748

pd.DataFrame({"Course ID" : course_ids}).to_csv('course_ids.csv')
