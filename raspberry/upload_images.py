import os
import requests

from datetime import datetime
from werkzeug.utils import secure_filename

content_type = 'image/jpeg'
server_ip_address = '192.168.192.9'
server_port = '5000'

datetime_stop = datetime(2018, 12, 25, 22, 00)

while((datetime_stop-datetime.now()).days >= 0):
  print('Stopping in {} seconds (at {})'.format((datetime_stop-datetime.now()).seconds, datetime_stop))
  filename = '{}_{}.{}'.format(
    'image',
    str(datetime.now()),
    'jpg')
  print("Capturing image: {}".format(filename))
  os.system('raspistill -o "{}"'.format(filename))

  files = {'file' : (filename, open(filename, 'rb'), content_type)}

  response = requests.post('http://{}:{}'.format(server_ip_address, server_port), files=files)

  if response.status_code == 200:
    bash_command = 'rm "{}"'.format(filename)
    print('Deleting: {}'.format(filename))
    os.system(bash_command)

