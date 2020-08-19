import requests
import json
import os
import configparser
config = configparser.ConfigParser()
from date_functions import add_date_range_to_params
from read_env import get_api_key

# redmine_api_key = get_api_key()
headers = {"Content-Type": "application/json", "origin": "https://cors-anywhere.herokuapp.com/"}
proxy = 'http://reverse-proxy:80'

def fetch_time_entries(harvard_project_id, api_key): 
  params = {} 
  params = add_date_range_to_params()
  params['project_id'] = harvard_project_id
  params['limit'] = 100

  headers['X-Redmine-Api-Key'] = api_key

  r = requests.get(f'{proxy}/time-entries', headers = headers, params=params)
  response = r.json()
  entries = response.get('time_entries')
  return entries
  
def fetch_project_details(api_key):
  params = {'include': 'time_entry_activities'}
  headers['X-Redmine-Api-Key'] = api_key

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