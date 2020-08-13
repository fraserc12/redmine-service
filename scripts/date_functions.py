import datetime
import calendar

date_format_str = '%Y-%m-%d'

def add_date_range_to_params():
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

def get_date_dtring(date):
  datetime_obj = get_date_object(date)
  return datetime_obj.date().strftime("%d %b %Y")

def get_day(date):
  datetime_obj = get_date_object(date)
  return datetime_obj.date().strftime('%A')

def get_date_object(date):
  return datetime.datetime.strptime(date, date_format_str)

# def get_current_date_range():
#   date_range = []
#   sdate = datetime.date(int(year), int(month), 1)
#   edate = datetime.date(int(year), int(month), int(day))

#   delta = edate - sdate       # as timedelta

#   for i in range(delta.days + 1):
#     dayNow = sdate + datetime.timedelta(days=i)
#     date_range.append(str(dayNow))

#   return date_range