#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 20:29:37 2025

@author: ulhvit
"""
import sqlite3


### Connect to SQL ###
class manage_db:
    def __init__(self, path_to_db):
        self.con = sqlite3.connect(path_to_db)
        self.cur = self.con.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS yt_watch_hist (
        title TEXT,
        channel TEXT,
        timestamp DATETIME,
        link TEXT,
        UNIQUE (timestamp, link)
        )
        """)

    def insert_row(self, tuple_row):        
        self.cur.execute("""
        INSERT OR IGNORE INTO yt_watch_hist (title, channel, timestamp, link)
        VALUES (?, ?, ?, ?)
        """, tuple_row)
        
    def commit_(self):
        self.con.commit()
    
    def close_conn(self):
        self.con.commit() #just in case
        self.con.close()