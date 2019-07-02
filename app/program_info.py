import os
import time

from .models import Radios, Program
from . import CONFIG

################################################################################################################################################################
# Program Info
################################################################################################################################################################

class ProgramsInfo:
  radio = Radios()
  program = Program()
  week_day_letters = ['Lun','Mar','Mie','Jue','Vie','Sab','Dom']
  timezone = 0
  week_day = 0
  list_week_day = 0

  def __init__(self,radio):
    self.radio = radio
    self.timezone = self.timezone()
    self.week_day = self.act_week_day()
    self.list_week_day = self.week_day
    self.program_update()

  # ---> Set Week Day
  def week_day_letter(self,wday):

    if int(wday) in [0,1,2,3,4,5,6]:
      return self.week_day_letters[int(wday)]

  # ---> Set Week Day
  def set_list_week_day(self,wday):

    if int(wday) in [0,1,2,3,4,5,6]:
      self.list_week_day = wday

  # ---> Progams List
  def program_list(self):

    self.radio.program_list.sort(key=lambda x: x.times)

    return self.radio.program_list

  # ---> TimeZone
  def timezone(self):

    if self.radio.country in CONFIG.TIMEZONES:
      timezone = CONFIG.TIMEZONES[self.radio.country]
    else:
      timezone = 0

    return timezone
      
  # ---> Actual Week Day
  def act_hour(self):
        
    act_hour = int(time.localtime().tm_hour) + self.timezone
    act_hour = act_hour % 24
        
    return act_hour

  # ---> Actual Week Day
  def act_week_day(self):
        
    act_wday = time.localtime().tm_wday
    act_hour = int(time.localtime().tm_hour) + self.timezone

    if act_hour < 0:
      act_wday = act_wday - 1
    if act_hour > 23:
      act_wday = act_wday + 1
        
    return act_wday

  # ---> Radio Time
  def radio_time_day(self):

    act_wday = self.act_week_day()

    act_h = self.act_hour()
    if act_h < 10:
      act_h_txt = '0' + str(act_h)
    else:
      act_h_txt = str(act_h)

    act_m = int(time.localtime().tm_min)
    if act_m < 10:
      act_m_txt = '0' + str(act_m)
    else:
      act_m_txt = str(act_m)

    str_h = act_h_txt + ':' + act_m_txt + ' [ ' + self.week_day_letter(act_wday) + ' ]'

    return str_h


  # ---> Check if Program is Live
  def is_prog_today(self,program):

    prog_wdays = program.week_days.split(',')
        
    return (str(self.list_week_day) in prog_wdays)


  # ---> Check Program Live
  def is_prog_live(self,program):

    act_h = self.act_hour()

    act_m = int(time.localtime().tm_min)
    act_day_m = act_h * 60 + act_m

    prog_wdays = program.week_days.split(',')

    prog_ini_h = int(program.times.split('-')[0].split(':')[0])
    prog_ini_m = int(program.times.split('-')[0].split(':')[1])

    prog_end_h = int(program.times.split('-')[1].split(':')[0])
    prog_end_m = int(program.times.split('-')[1].split(':')[1])

    prog_day_ini_m = prog_ini_h * 60 + prog_ini_m
    prog_day_end_m = prog_end_h * 60 + prog_end_m

    return ( (str(self.act_week_day()) in prog_wdays) and (act_day_m >= prog_day_ini_m) and (act_day_m < prog_day_end_m) )

  # ---> Program Time
  def program_update(self):

    self.program = None

    for program in self.radio.program_list:
      if self.is_prog_live(program):
        self.program = program

  
  # ---> Program Time
  def program_time(self):

    self.program_update()

    if self.program:
      prog_ini_h = int(self.program.times.split('-')[0].split(':')[0])
      prog_ini_m = int(self.program.times.split('-')[0].split(':')[1])

      prog_end_h = int(self.program.times.split('-')[1].split(':')[0])
      prog_end_m = int(self.program.times.split('-')[1].split(':')[1])

      prog_day_ini_m = prog_ini_h * 60 + prog_ini_m
      prog_day_end_m = prog_end_h * 60 + prog_end_m

      prog_time_s = (prog_day_end_m - prog_day_ini_m) * 60
        
      return prog_time_s

    else:

      return 0


  # ---> Program Elapsed Time
  def program_elapsed_time(self):

    self.program_update()

    if self.program:
      act_h = self.act_hour()
      act_m = int(time.localtime().tm_min)

      act_day_m = act_h * 60 + act_m

      prog_ini_h = int(self.program.times.split('-')[0].split(':')[0])
      prog_ini_m = int(self.program.times.split('-')[0].split(':')[1])

      prog_day_ini_m = prog_ini_h * 60 + prog_ini_m

      prog_elapsed_time_s = (act_day_m - prog_day_ini_m) * 60
          
      return prog_elapsed_time_s

    else:

      return 0

