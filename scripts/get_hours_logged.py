import requests
from itertools import groupby
from fetch import *
from date_functions import *
from time_entry import TimeEntry
from operator import itemgetter

def construct_hour_summary(entries):
  hour_summary = []
  #group entries by Date
  for spent_on, time_entries in groupby(entries, key=itemgetter('spent_on')):
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

def select_project(projects):
  valid_project_id = []
  for i in range(len(projects)):
    print(f'{i+1}: {projects[i].get("name")}')
    valid_project_id.append(i)

  project_selection = int(input('\nSelect Project: ')) - 1

  while not (project_selection in valid_project_id):
    print("\nInvalid Project! Try again.. \n")
    project_selection = int(input('\nSelect Project: ')) - 1

  return project_selection

def print_summary(summary):
  print("\n-- Summary --\n")
  #reversed cos redmine does it from today backwards - not a fan
  for entry in reversed(summary):
    print(entry)


all_projects = fetch_project_details()
project_selected = select_project(all_projects)
entries = fetch_time_entries(all_projects[project_selected].get('id'))
if not entries:
  print("\nNo time entries found!")
else:
  hour_summary = construct_hour_summary(entries)
  print_summary(hour_summary)