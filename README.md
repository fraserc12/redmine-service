# redmine-service

This command line Python script will do a lookback of time entries, depending on the current date, for either:
- 1st to 15th 
- 15th to Last day of current month

As our time entries are submitted in the middle of the month and at the end. 

**Note:** Only dates with time entries will be printed

## Why
I was fed up of checking Redmine's UI to see if I had looged 8 hours per day - especially when it came to "redmine day"

### Set Up
* Docker 
* Python3 - https://www.python.org/downloads/
* Get your Redmine API key and set the `redmine_api_key` variable in the **env.ini** file

### To Run 
- From the root directory: `pip3 install -r requirements.txt` to install dependencies
- From the root directory: `docker-compose up` to spin up reverse proxy
- From the `./scripts` directory: `python3 get_hours_logged.py`
- Then select your project when command line prompts you

### Disclaimer
I am new to Python - this code works but will probably be improved upon when I learn more.  
Feel free to fork and submit Pull Request
