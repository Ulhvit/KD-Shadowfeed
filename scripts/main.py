#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 14:50:57 2025

@author: ulhvit
"""
import sqlite3
import sql_load as sqll
import extract_from_html
from vid_data_cleaner import clean_entry

### Paths ### 
WATCH_HIST = "/home/ulhvit/Storage/KD-Shadowfeed/KD-Shadowfeed/data/watch_hist.html"
WATCH_HIST_DB = "/home/ulhvit/Storage/KD-Shadowfeed/KD-Shadowfeed/db/yt_watch_history.db"
### ETL PIPELINE ###

sqll.create_db()

for data_row in extract_from_html(WATCH_HIST):
    cleaned_data_row = clean_entry(data_row)
    sqll.insert_row(cleaned_data_row)
    
conn = sqlite3.Connection(WATCH_HIST_DB)
cur = conn.cursor()
###test the db ###
cur.execute("""SELECT * FROM yt_watch_hist
               ORDER BY timestamp DESC
               LIMIT 10""")

    
