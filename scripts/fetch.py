import requests
import json
import os
import configparser
config = configparser.ConfigParser()
from date_functions import add_date_range_to_params

config.read('env.ini')
redmine_api_key = config['redmine']['redmine_api_key']
headers = {"Content-Type": "application/json", "X-Redmine-Api-Key": redmine_api_key, "origin": "https://cors-anywhere.herokuapp.com/"}
proxy = 'http://reverse-proxy:80'

def fetch_time_entries(harvard_project_id): 
  params = {} 
  params = add_date_range_to_params()
  params['project_id'] = harvard_project_id
  params['limit'] = 100

  r = requests.get(f'{proxy}/time-entries', headers = headers, params=params)
  response = r.json()
  entries = response.get('time_entries')
  return entries
  
def fetch_project_details():
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