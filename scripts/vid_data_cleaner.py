#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 12:29:26 2025

@author: ulhvit
"""

import unicodedata
import re

# Regex to remove emoji / symbols outside the BMP
_EMOJI_PATTERN = re.compile( ## IMPORTANT: CHECK RANGES, they don't seem okay
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U00002702-\U000027B0"  # dingbats
    "\U000024C2-\U0001F251"  # enclosed characters
    "]+",
    flags=re.UNICODE
)

def sanitize_text(s: str) -> str | None:
    """
    Clean a string so it's safe for database insertion:
    - Normalize Unicode
    - Remove emojis
    - Remove control/non-printable chars
    - Collapse spaces
    """
    if not s:
        return None

    # Normalize accents, weird forms (e.g. fullwidth chars)
    s = unicodedata.normalize("NFKC", s)

    # Remove emoji
    s = _EMOJI_PATTERN.sub("", s)

    # Remove control chars / non-printable
    s = re.sub(r"[\x00-\x1F\x7F]", "", s)

    # Collapse whitespace
    s = re.sub(r"\s+", " ", s)

    return s.strip()

def clean_entry(entry):
    entry = [sanitize_text(string_) for string_ in entry if string_ and string_.strip()]
    entry = [string_ for string_ in entry if not string_.lower().startswith("obejrzano")]

    link, title, channel, timestamp_str = entry

    month_map = {
        "sty": "01", "lut": "02", "mar": "03", "kwi": "04",
        "maj": "05", "cze": "06", "lip": "07", "sie": "08",
        "wrz": "09", "paz": "10", "lis": "11", "gru": "12"
    }

    match = re.match(r"(\d{1,2}) (\w{3}) (\d{4}), (\d{2}:\d{2}:\d{2})", timestamp_str)
    if match:
        day, mon_abbr, year, time_str = match.groups()
        month = month_map[mon_abbr.lower()]
        watched_at = f"{year}-{month}-{int(day):02d} {time_str}"
    else:
        watched_at = None

    return (
        sanitize_text(link),
        sanitize_text(title),
        sanitize_text(channel),
        sanitize_text(watched_at)
    )
