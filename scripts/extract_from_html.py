#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 19:18:55 2025

@author: ulhvit
"""
from lxml import etree

### Functions ###
#@profile
def extract_watch_data(WATCH_HIST):
    ''' 

    Parameters
    ----------
    WATCH_HIST : TYPE string - path to html file
        Parses an HTML tree to extract text and links from a specific section.

        Iterates over a target set of <div> elements, collects text 
        withing tags and the first hyperlink, and returns the results as a list. 
        Frees processed nodes from memory to reduce overhead 
        when handling large documents.

    Yields
    ------
    list_for_sql : TYPE list
        list of 5 elements, containing a link and 4 unprocessed strings 

    '''
    target_class = "content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1"
    context = etree.iterparse(WATCH_HIST, html=True, tag="div")
    for _, thing in context:
        if thing.attrib.get("class", "").strip() == target_class:
            first_a = thing.find(".//a")
            watched_vid_link = first_a.attrib.get("href",'')
            text_in_cell = [text_ for text_ in thing.itertext()]
            while len(text_in_cell) < 4:
                text_in_cell.insert(-1, None)
            # [1:] to skip "obejrzano/watched"
            list_for_sql = text_in_cell[1:] + [watched_vid_link] 
            yield list_for_sql
    # ---------------- MEMORY CLEANS -----------------
        thing.clear() # Clear the current element's children.
        while thing.getprevious() is not None: # Remove references to all previous siblings of the element
            del thing.getparent()[0]
    del context
