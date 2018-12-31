import re

from argparse import ArgumentTypeError
from datetime import datetime

def datetime_format_type(string):
  pattern = '(\d{4})-([0-1]\d)-([0-3]\d)T([0-2]\d):?([0-5][\d])?:?([0-5][\d])?'
  # print(re.match(pattern, string))
  if not re.match(pattern, string):
    raise ArgumentTypeError('Please provide correct datetime in the following format: YYYY-MM-DDTHH[:MM][:SS]')
  return datetime(*tuple(int(x) for x in re.findall(pattern, string)[0]))

# print(datetime_format_type('2018-12-22T12:30:40'))