#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 12:29:26 2025

@author: ulhvit
"""

import re
import unicodedata

# TODO: Unicode ranges. These don't seem to be... sensible and are out of order
_EMOJI_PATTERN = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F1E6-\U0001F1FF"  # flags
    "\U00002600-\U000026FF"  # miscellaneous symbols
    "\U00002700-\U000027BF"  # dingbats
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols & Pictographs (includes 🧠)
    "\U0001FA70-\U0001FAFF"  # Symbols & Pictographs Extended-A
    "]+",
    flags=re.UNICODE
)

def sanitize_text(s):
    """
    Remove emojis and non-printable junk, normalize unicode, collapse whitespace.
    Returns None for false input.
    """
    if not s:
        return None

    # Normalize Unicode forms (compat/composed)
    s = unicodedata.normalize("NFKC", s)

    # Remove emoji characters (covers many emoji blocks, including the brain)
    s = _EMOJI_PATTERN.sub("", s)

    # Remove emoji joiners/variation selectors that sometimes remain
    s = s.replace("\ufe0f", "")  # variation selector-16
    s = s.replace("\u200d", "")  # zero-width-joiner

    # Normalize whitespace (convert newlines/tabs to spaces)
    s = re.sub(r"[\t\n\r\f\v]+", " ", s)

    # Remove ASCII control chars (if any left)
    s = re.sub(r"[\x00-\x1F\x7F]", "", s)

    # Collapse multiple spaces and strip ends
    s = re.sub(r"\s+", " ", s).strip()

    return s

def watched_at_datetime_conversion(timestamp_str):
    """
    Convert a YouTube watch history timestamp (Polish locale) into
    a SQL-compatible datetime string.

    Input format (example):
        "23 lip 2025, 17:04:10"

    Args:
        timestamp_str (str): Raw timestamp string from YouTube watch history.

    Returns:
        str | None: A datetime string in "YYYY-MM-DD HH:MM:SS" format,
                    or None if conversion fails.
    """
    month_map = {
        "sty": "01", "lut": "02", "mar": "03", "kwi": "04",
        "maj": "05", "cze": "06", "lip": "07", "sie": "08",
        "wrz": "09", "paz": "10", "lis": "11", "gru": "12"
    }
    match = re.match(r"(\d{1,2}) (\w{3}) (\d{4}), (\d{2}:\d{2}:\d{2})", timestamp_str)
    if match:
        day, mon_abbr, year, time_str = match.groups()
        month = month_map[mon_abbr.lower()]
        #int(day):02d for making sure 0 is included for proper datetime
        #month 0 padding is covered from the month_map
        watched_at_clean = f"{year}-{month}-{int(day):02d} {time_str}" 
    else:
        watched_at_clean = None #for failed cleaning/mapping
    return watched_at_clean

def clean_entry(entry):
    #Sanitize entry
    entry = [sanitize_text(string_) for string_ in entry if string_]
    #Get rid of "Obejrzano"
    entry = [s for s in entry if not s.lower().startswith("obejrzano")]
    link, title, channel, timestamp_str = entry
    #date conversion mapping
    watched_at_clean = watched_at_datetime_conversion(timestamp_str)
    #end of date conversion mapping. Returns tuple
    return (
        title,
        channel,
        watched_at_clean,
        link
    )
