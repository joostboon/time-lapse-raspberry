import functools

from datetime import datetime

def minute_timer(func):
  @functools.wraps(func)
  def wrapper_timer(*args, **kwargs):
    while datetime.now().second != 0:
      pass
    value = func()
    return value
  return wrapper_timer