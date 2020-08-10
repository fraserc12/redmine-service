#!/usr/local/bin/python3
from date_functions import *

class TimeEntry:
  holiday_activity = "Vacation/PTO/Holiday"

  def isVacationDay(self, logged_activity):
    if(logged_activity == self.holiday_activity):
      return True
    else:
      return False

  def __init__(self, date, hours, activity):
    self.day = getDay(date)
    self.date = date
    self.hours = str(hours)
    self.isHoliday = self.isVacationDay(activity)
  
  def __str__(self):
    isHol = ''
    br = ''
    if(self.isHoliday):
      isHol = self.holiday_activity
    if(self.day == 'Friday'):
      br = '\n'
    return f'On {self.day} [{self.date}] you logged {self.hours} hours {isHol}{br}'