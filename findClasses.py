import requests
import csv
import json
import pandas as pd
import numpy as np

def c(s): # Y → 1, N → 0
    if "Y" in s:
        return 1
    return 0
    
# Get each class's info for each course ID and store it

courseIDs = pd.read_csv('course_ids.csv')

# MASTER DICTIONARY

mD = {'CourseID':[],
      'Subject': [],
      'Number' : [],
      'Course Name' : [],
      'Professor': [],
      'Room': [],
      'Start': [],
      'End': [],
      'Monday': [],
      'Tuesday': [],
      'Wednesday': [],
      'Thursday': [],
      'Friday': []}
# course offer number is 1 so no cross listings
#for i in range(20):
for i in range(len(courseIDs)):
    courseID = courseIDs["Course ID"][i]
    spec_url = "https://streamer.oit.duke.edu/curriculum/classes/strm/" + term + "/crse_id/" + str(courseID) + "?crse_offer_nbr=1&access_token=" + access
    
    try: # SOMETIMES THE CLASS CODES DO NOT WORK, THUS THE TRY | EXCEPT 
        spec_cont = requests.get(url = spec_url).json() 
    except: 
        print('failed: ' + str(courseID))
        continue
    
    num_crse = int(spec_cont["ssr_get_classes_resp"]["search_result"]["ssr_course_count"])
    num_classes = int(spec_cont["ssr_get_classes_resp"]["search_result"]["ssr_class_count"])
    
    if(num_crse == 0): # NOT OFFERED THIS TERM
        #print(str(courseID) + ": NOT OFFERED")
        continue
        
    print("Course: " + str(courseID) +" has " + str(num_classes) + " classes.")
    
    f = spec_cont["ssr_get_classes_resp"]["search_result"]["subjects"]["subject"]["classes_summary"]["class_summary"] #focused
    
    if num_classes == 1:
        mp = f["classes_meeting_patterns"]["class_meeting_pattern"] # meeting pattern
        
        try:
            if("Online Course" in mp["ssr_mtg_loc_long"]):
                continue

            if("TBA" in mp["ssr_mtg_loc_long"]):
                continue
        except:
            
            print("Weird Case: " + str(courseID))
            
            for j in range(len(mp)):
                if("Online Course" in mp[j]["ssr_mtg_loc_long"]):
                    continue

                if("TBA" in mp[j]["ssr_mtg_loc_long"]):
                    continue
                    
                mD['CourseID'].append(f['crse_id'])
                mD['Subject'].append(f['subject'])
                mD['Number'].append(f['catalog_nbr'])
                mD['Course Name'].append(f["crse_id_lov_descr"])
                mD['Professor'].append(mp[j]["ssr_instr_long"])
                mD['Room'].append(mp[j]["ssr_mtg_loc_long"])
                mD['Start'].append(mp[j]["meeting_time_start"][11:16])
                mD['End'].append(mp[j]["meeting_time_end"][11:16])
                mD['Monday'].append(c(mp[j]["mon"]))
                mD['Tuesday'].append(c(mp[j]["tues"]))
                mD['Wednesday'].append(c(mp[j]["wed"]))
                mD['Thursday'].append(c(mp[j]["thurs"]))
                mD['Friday'].append(c(mp[j]["fri"]))

                pd.DataFrame(mD).to_csv('Spring_2021.csv')
            continue
            
        mD['CourseID'].append(f['crse_id'])
        mD['Subject'].append(f['subject'])
        mD['Number'].append(f['catalog_nbr'])
        mD['Course Name'].append(f["crse_id_lov_descr"])
        mD['Professor'].append(mp["ssr_instr_long"])
        mD['Room'].append(mp["ssr_mtg_loc_long"])
        mD['Start'].append(mp["meeting_time_start"][11:16])
        mD['End'].append(mp["meeting_time_end"][11:16])
        mD['Monday'].append(c(mp["mon"]))
        mD['Tuesday'].append(c(mp["tues"]))
        mD['Wednesday'].append(c(mp["wed"]))
        mD['Thursday'].append(c(mp["thurs"]))
        mD['Friday'].append(c(mp["fri"]))
        
        pd.DataFrame(mD).to_csv('Spring_2021.csv')
        continue
        
        
    for i in range(num_classes):
        mp = f[i]["classes_meeting_patterns"]["class_meeting_pattern"]
            
        try:
            if("Online Course" in mp["ssr_mtg_loc_long"]):
                continue

            if("TBA" in mp["ssr_mtg_loc_long"]):
                continue
        except:
            
            print("Weird Case: " + str(courseID))
            
            for j in range(len(mp)):
                if("Online Course" in mp[j]["ssr_mtg_loc_long"]):
                    continue

                if("TBA" in mp[j]["ssr_mtg_loc_long"]):
                    continue
                    
                mD['CourseID'].append(f[i]['crse_id'])
                mD['Subject'].append(f[i]['subject'])
                mD['Number'].append(f[i]['catalog_nbr'])
                mD['Course Name'].append(f[i]["crse_id_lov_descr"])
                mD['Professor'].append(mp[j]["ssr_instr_long"])
                mD['Room'].append(mp[j]["ssr_mtg_loc_long"])
                mD['Start'].append(mp[j]["meeting_time_start"][11:16])
                mD['End'].append(mp[j]["meeting_time_end"][11:16])
                mD['Monday'].append(c(mp[j]["mon"]))
                mD['Tuesday'].append(c(mp[j]["tues"]))
                mD['Wednesday'].append(c(mp[j]["wed"]))
                mD['Thursday'].append(c(mp[j]["thurs"]))
                mD['Friday'].append(c(mp[j]["fri"]))
                
            pd.DataFrame(mD).to_csv('Spring_2021.csv')
            continue
            
        mD['CourseID'].append(f[i]['crse_id'])
        mD['Subject'].append(f[i]['subject'])
        mD['Number'].append(f[i]['catalog_nbr'])
        mD['Course Name'].append(f[i]["crse_id_lov_descr"])
        mD['Professor'].append(mp["ssr_instr_long"])
        mD['Room'].append(mp["ssr_mtg_loc_long"])
        mD['Start'].append(mp["meeting_time_start"][11:16])
        mD['End'].append(mp["meeting_time_end"][11:16])
        mD['Monday'].append(c(mp["mon"]))
        mD['Tuesday'].append(c(mp["tues"]))
        mD['Wednesday'].append(c(mp["wed"]))
        mD['Thursday'].append(c(mp["thurs"]))
        mD['Friday'].append(c(mp["fri"]))
        
    pd.DataFrame(mD).to_csv('Spring_2021.csv')
print(pd.DataFrame(mD))
