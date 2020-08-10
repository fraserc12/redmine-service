#!/usr/local/bin/python3
import requests
import pylint.reporters.json_reporter
from itertools import groupby
from fetch import *
from date_functions import *
from time_entry import TimeEntry

harvard_project_id = '573'

def constructHourSummary(entries):
  hour_summary = []
  #group entries by Date
  for spent_on, time_entries in groupby(entries, lambda x: x['spent_on']):
    total_hours = 0
    date = ''
    activity = ''
    # Get Date and accumulative total of hours per day
    for time_entry in time_entries:
      total_hours += time_entry['hours']
      date = spent_on
      activity = time_entry['activity'].get('name')

    entry = TimeEntry(date, total_hours, activity)
    hour_summary.append(entry)

  return hour_summary

def printSummary(summary):
  print("\n")
  #reversed cos redmine does it from today backwards - not a fan
  for entry in reversed(summary):
    print(entry)

# fetchProjectDetails()
entries = fetchTimeEntries(harvard_project_id)
hour_summary = constructHourSummary(entries)
printSummary(hour_summary)