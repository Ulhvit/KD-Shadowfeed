#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 20:29:37 2025

@author: ulhvit
"""
import sqlite3

DATABASE_PATH = "/home/ulhvit/Storage/KD-Shadowfeed/KD-Shadowfeed/db/yt_watch_history.db"

### Connect to SQL ###
def create_db():

    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()

    # create table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS yt_watch_hist (
    title TEXT,
    channel TEXT,
    timestamp DATETIME,
    link TEXT
    UNIQUE (timestamp)
    )
    """)

    con.commit()
    con.close()
    

def insert_row(tuple_row):
    
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()
    
    cur.execute("""
    INSERT INTO yt_watch_hist (title channel timestamp link)
    VALUES (?, ?, ?, ?))
    """, tuple_row)
    
    con.commit()
    con.close()
