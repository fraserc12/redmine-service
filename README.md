# redmine-service

This command line Python script will do a lookback of time entries, for the current month, for either:
- 1st to 15th 
- 15th to Last day of month

Depending on the current date.

## Why
I was fed up of checking Redmine's UI to see if I had looged 8 hours per day - especially when it came to "redmine day"

### Set Up
* Docker
* Python3
* Get your Redmine API key and set environment variable on your OS called `redmine_api_key`
- On Mac OS for example: `export redmine_api_key='<key>'`

### To Run 
- From the root directory: `pip3 install -r requirements.txt` to install dependencies
- From the root directory: `docker-compose up` to spin up reverse proxy
- From the `./scripts` directory Simply run `python3 get_hours_logged.py`
- Then select your project when command line prompts you

### Disclaimer
I am new to Python - this code works but will probably be improved upon when I learn more
