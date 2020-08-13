#!/usr/local/bin/python3
import requests
import json
from date_functions import addDateRangeToParams

redmine_api_key = "524cb5a3946f9170333ce59b45d52eace5b44224"
headers = {"Content-Type": "application/json", "X-Redmine-Api-Key": redmine_api_key, "origin": "https://cors-anywhere.herokuapp.com/"}
proxy = 'http://localhost:8383'

def fetchTimeEntries(harvard_project_id): 
  params = {} 
  params = addDateRangeToParams()
  params['project_id'] = harvard_project_id
  params['limit'] = 100

  r = requests.get(f'{proxy}/time-entries', headers = headers, params=params)
  response = r.json()
  entries = response.get('time_entries')
  return entries
  
def fetchProjectDetails():
  params = {'include': 'time_entry_activities'}

  r = requests.get(f'{proxy}/projects', headers = headers, params=params)
  response = r.json()
  projects = response.get("projects")

  project_options = []

  for p in projects:
    project_name = p.get('name')
    project_id = p.get('id')
    if(p.get('status') == 1):
      project = {'id': project_id, 'name': project_name}
      project_options.append(project)

  return project_options