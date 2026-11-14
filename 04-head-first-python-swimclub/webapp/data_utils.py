"""Database utilities for the swim club webapp.

Function                 Query                                    Parameters
-----------------------  ---------------------------------------  --------------------------------------
get_swim_sessions        SQL_SESSIONS                             none
get_session_swimmers     SQL_SWIMMERS_BY_SESSION                  date
get_swimmers_events      SQL_SWIMMERS_EVENTS_BY_SESSION           name, age, date
get_swimmers_times       SQL_CHART_DATA_BY_SWIMMER_EVENT_SESSION  name, age, distance, stroke, date
"""

import DBcm

## db_details = "CoachDB.sqlite3"

import platform

if "aws" in platform.uname().release:
    #running on Pythonanywhere.
    db_details = {
        "host": "giatuong0.mysql.pythonanywhere-services.com",
        "database": "giatuong0$default",
        "user": "giatuong0",
        "password": "swimpasswd"
    }
else:
    #running locally.
    db_details = {
    "host": "localhost",
    "database": "swimDB",
    "user": "swimuser",
    "password": "swimpasswd"
}
# NOTE: password hardcoded for learning only.
# In production, load it from an environment variable or .env file (not git).


from queries import *

from pathlib import Path

##db_details = str(Path(__file__).parent / "CoachDB.sqlite3") #ai code to fix path but no longer needed becuz changed to mariaDB

def get_swim_sessions():
    """Return a tuple-list of unique session timestamps."""
    with DBcm.UseDatabase(db_details) as db:
        db.execute(SQL_SESSIONS)
        results = db.fetchall()
    return results


def get_session_swimmers(date):
    """When given a date (YYYY-MM-DD), return a tuple-list of swimmers
    and their associated age (filtered by date).
    """
    with DBcm.UseDatabase(db_details) as db:
        db.execute(SQL_SWIMMERS_BY_SESSION, (date,))
        results = db.fetchall()
    return results


def get_swimmers_events(name, age, date):
    """When given a date (YYYY-MM-DD), swimmer's name, and swimmer's age, return
    a tuple-list of events the swimmer swam on that date."""
    with DBcm.UseDatabase(db_details) as db:
        db.execute(SQL_SWIMMERS_EVENTS_BY_SESSION, (name, age, date,))
        results = db.fetchall()
    return results


def get_swimmers_times(name, age, distance, stroke, date):
    """When given a date (YYYY-MM-DD), swimmer's name, age, distance, and stroke,
    return a tuple-list of times the swimmer swam on that date over the identified
    distance/stroke combination."""
    with DBcm.UseDatabase(db_details) as db:
        db.execute(
            SQL_CHART_DATA_BY_SWIMMER_EVENT_SESSION,
            (name, age, distance, stroke, date,),
        )
        results = db.fetchall()
    return results


# queries.py says what to ask inside "CoachDB.sqlite3", 
# data_utils.py asks it and returns the answer, 
# and app.py uses the answer.