#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 14:50:57 2025

@author: ulhvit
"""
import sql_load as sqll
import extract_from_html
from vid_data_cleaner import clean_entry

### Paths ### 
WATCH_HIST = "/home/ulhvit/Storage/KD-Shadowfeed/KD-Shadowfeed/data/watch_hist.html"
WATCH_HIST_DB = "/home/ulhvit/Storage/KD-Shadowfeed/KD-Shadowfeed/db/yt_watch_history.db"
### ETL PIPELINE ###

sql_db = sqll.manage_db(WATCH_HIST_DB)
count = 0
batch_size = 100

for data_row in extract_from_html.extract_watch_data(WATCH_HIST):
    cleaned_data_row = clean_entry(data_row)
    sql_db.insert_row(cleaned_data_row)
    count+=1
    if count % batch_size == 0:
        sql_db.commit_()

sql_db.commit_()
sql_db.close_conn()

print("Database ready")
    
