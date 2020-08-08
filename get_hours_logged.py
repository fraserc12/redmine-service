#!/usr/local/bin/python3
import requests
import pylint.reporters.json_reporter
from itertools import groupby
from fetch import *
from date_functions import *

harvard_project_id = '573'
holiday_activity = "Vacation/PTO/Holiday"

def isVacationDay(logged_activity):
  if(logged_activity == holiday_activity):
    return True
  else:
    return False

def constructHourSummary(entries):
  hour_summary = []
  #group entries by Date
  for spent_on, time_entries in groupby(entries, lambda x: x['spent_on']):
    total_hours = 0
    date = ''
    is_holiday = False
    # Get Date and accumulative total of hours per day
    for time_entry in time_entries:
      total_hours += time_entry['hours']
      date = spent_on
      is_holiday = isVacationDay(time_entry['activity'].get('name'))

    entry = {'date': date, 'totalHours': total_hours, 'isHoliday': is_holiday}
    hour_summary.append(entry)

  return hour_summary

def printSummary(summary):
  print("\n")
  #reversed cos redmine does it from today backwards - not a fan
  for h in reversed(summary):
    #Get the Day
    date = getDateString(h['date'])
    day = getDay(h['date'])
    isHol = ''
    if(h['isHoliday']):
      isHol = holiday_activity
    print(f'On {day} [{date}] you logged {str(h["totalHours"])} hours {isHol}')
    if(day == 'Friday'):
      print("\n")


# fetchProjectDetails()
entries = fetchTimeEntries(harvard_project_id)
hour_summary = constructHourSummary(entries)
printSummary(hour_summary)