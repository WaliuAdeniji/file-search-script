import os
from dateutil import parser
import datetime

#Recommended format for start and end date is YYYY-MM-DD

def search(start:str, end:str):
  #convert to datetime object
  start = parser.parse(start).date()
  end = parser.parse(end).date()

  if start > end:
    return f"Check again, your 'start' date: {start}, should be less than your 'end' date: {end}"

  return [(line + " >> file") if '.' in line else (line + " >> folder") \
          for line in os.listdir()\
          if (datetime.datetime.fromtimestamp(os.path.getmtime(line)).date()>=start)\
          and (datetime.datetime.fromtimestamp(os.path.getmtime(line)).date()<=end)]


def by_filename(start:str, end:str, filename:str):
  start = parser.parse(start).date()
  end = parser.parse(end).date()

  if start > end:
    return f"Check again, your 'start' date: {start}, should be less than your 'end' date: {end}"

  return [(line) for line in os.listdir() if (filename in line) and \
          (datetime.datetime.fromtimestamp(os.path.getmtime(line)).date()>=start)\
          and (datetime.datetime.fromtimestamp(os.path.getmtime(line)).date()<=end)]


def in_folder(start:str, end:str):
  start = parser.parse(start).date()
  end = parser.parse(end).date()

  if start > end:
    return f"Check again, your 'start' date: {start}, should be less than your 'end' date: {end}"

  return [(file) for root,dir,files in os.walk('.') for file in files \
          if (datetime.datetime.fromtimestamp(os.path.getmtime(root)).date()>=start)\
          and (datetime.datetime.fromtimestamp(os.path.getmtime(root)).date()<=end)]


start = str(input("Your start date: "))
end = str(input("Your end date: "))
#filename = str(input("Your file name is:")) #uncomment only when searching by filename

#print(search(start, end))  #search for matched files/folders within cwd
#print(by_filename(start,end, filename))  #search by filename within cwd
#print(in_folder(start, end))  #search files & within folders in cwd