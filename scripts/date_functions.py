#!/usr/local/bin/python3
import datetime
import calendar

date_format_str = '%Y-%m-%d'

def addDateRangeToParams():
  today = datetime.datetime.now()
  day = today.strftime("%d")
  month = today.strftime("%m")
  year = today.strftime("%Y")
  last_day_of_month = str(calendar.monthrange(today.year, today.month)[1])

  first_half_month_date_range = [f'{year}-{month}-01', f'{year}-{month}-15']
  second_half_month_date_range = [f'{year}-{month}-15', f'{year}-{month}-{last_day_of_month}']

  params = {}
  if(int(day) < 16):
    params['from'] = first_half_month_date_range[0]
    params['to'] = first_half_month_date_range[1]
  else:
    params['from'] = second_half_month_date_range[0]
    params['to'] = second_half_month_date_range[1]

  return params

def getDateString(date):
  datetime_obj = getDateObject(date)
  return datetime_obj.date().strftime("%d %b %Y")

def getDay(date):
  datetime_obj = getDateObject(date)
  return datetime_obj.date().strftime('%A')

def getDateObject(date):
  return datetime.datetime.strptime(date, date_format_str)