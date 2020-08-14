from date_functions import *

class TimeEntry:
  holiday_activity = "Vacation/PTO/Holiday"

  def is_vacation_day(self, logged_activity):
    if(logged_activity == self.holiday_activity):
      return True
    else:
      return False

  def __init__(self, date, hours, activity):
    self.day = get_day(date)
    self.date = date
    self.hours = str(hours)
    self.isHoliday = self.is_vacation_day(activity)
  
  def __str__(self):
    isHol = ''
    br = ''
    if(self.isHoliday):
      isHol = f'({TimeEntry.holiday_activity})'
    if(self.day == 'Friday'):
      br = '\n'
    return f'{self.day} [{self.date}] - {self.hours} hours {isHol}{br}'