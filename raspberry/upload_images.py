import argparse
import os
import requests

from datetime import datetime, timedelta

from utils.decorators import minute_timer
from utils.helpers import datetime_format_type

parser = argparse.ArgumentParser()
time_group = parser.add_mutually_exclusive_group()

parser.add_argument("-p","--project_name", required=True, help="Provide a name for the project.")
time_group.add_argument("-l", "--length", help="Please provide number of minutes to record.", type=int)
time_group.add_argument("-e", "--end_date", type=datetime_format_type, help="Time at which time-lapse should stop. \
                                              Please provide in follwing format: YYYY-MM-DDTHH[:MM][:SS]")
cli_args = vars(parser.parse_args())

content_type = 'image/jpeg'
server_ip_address = ''
server_port = '5000'

print(cli_args)
if cli_args['end_date']:
  datetime_stop = cli_args['end_date']
elif cli_args['length']:
  datetime_stop = datetime.now() + timedelta(minutes=cli_args['length'])
else:
  # Setting default value but this should not be able to be called due to mutually exclusive group in argpars.
  datetime_stop = datetime.now() + timedelta(minutes=30)

while((datetime_stop-datetime.now()).days >= 0):

  @minute_timer
  def take_and_send_picture():
    print('Stopping in {} seconds (at {})'.format((datetime_stop-datetime.now()).seconds, datetime_stop))
    filename = '{}_{}.{}'.format(
      'image',
      str(datetime.now()),
      'jpg')
    print("Capturing image: {}".format(filename))
    os.system('raspistill -o "{}"'.format(filename))

    files = {'file' : (filename, open(filename, 'rb'), content_type)}

    response = requests.post('http://{}:{}/upload_picture/{}'.format(
            server_ip_address,
            server_port,
            cli_args['project_name']), files=files)

    if response.status_code == 200:
      bash_command = 'rm "{}"'.format(filename)
      print('Deleting: {}'.format(filename))
      os.system(bash_command)

  take_and_send_picture()

r = requests.post('http://{}:{}/create-time-lapse/{}'.format(server_ip_address, server_port, cli_args['project_name']))

