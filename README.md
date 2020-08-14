# redmine-service

This app will do a lookback of time entries, depending on the current date, for either:
- 1st to 15th 
- 15th to Last day of current month

As our time entries are submitted in the middle of the month and at the end. 

**Note:** Only dates with time entries will be printed

## Why
I was fed up of checking Redmine's UI to see if I had looged 8 hours per day - especially when it came to "redmine day"

### Set Up
* Docker 
* Get your Redmine API key and set the `redmine_api_key` variable in the **env.ini** file

### To Run 
- From the root directory: `docker-compose up`

## API Docs
2 endpoints are exposed on `http://localhost:5001`
- GET `/projects`  - returns details of all your projects
- GET `/time-logged?project_id=<id>` - will return a summarised list of time entries per day

### Disclaimer
I am new to Python - this code works but will probably be improved upon when I learn more.  
Feel free to submit Pull Request
