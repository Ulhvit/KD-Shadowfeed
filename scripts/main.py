#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 19:18:55 2025

@author: ulhvit
"""
from datetime import datetime
from lxml import etree
import dateparser
import sqlite3

### Paths ### 
WATCH_HIST = "/home/ulhvit/Storage/KD-Shadowfeed/KD-Shadowfeed/data/watch_hist.html"
SHADOWFEED_SQL_DB = "/home/ulhvit/Storage/KD-Shadowfeed/KD-Shadowfeed/db/yt_watch_history.db"
### Connect to SQL ###
#con = sqlite3.connect("/home/ulhvit/Storage/KD-Shadowfeed/KD-Shadowfeed/db/yt_watch_history.db")
#cur = con.cursor()

### Functions ###
def extract_watch_data(WATCH_HIST):
    target_class = "content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1"
    context = etree.iterparse(WATCH_HIST, html=True, tag="div")
    for _, thing in context:
        if thing.attrib.get("class", "").strip() == target_class:
            first_a = thing.find(".//a")
            watched_vid_link = first_a.attrib.get("href",'')
            text_in_cell = list(thing.itertext())
            list_for_sql = [watched_vid_link] + text_in_cell
            yield list_for_sql
    # ---------------- MEMORY CLEANS -----------------
        thing.clear() # Clear the current element's children.
        while thing.getprevious() is not None: # Remove references to all previous siblings of the element
            del thing.getparent()[0]
    del context
    
### main ###
