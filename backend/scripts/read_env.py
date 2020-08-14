import os
import configparser
config = configparser.ConfigParser()

#tidy this up...
def get_api_key():
  redmine_api_key = ''
  cwd = os.getcwd()
  if("script" in cwd):
    config.read('../env.ini')
    redmine_api_key = config['redmine']['redmine_api_key']
  else:
    config.read('env.ini')
    redmine_api_key = config['redmine']['redmine_api_key']

  return redmine_api_key