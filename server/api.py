import os

from datetime import datetime

from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
  if request.method == 'POST':
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join('uploads', '{}_{}.{}'.format(
      filename.split('.')[0],
      str(datetime.now()),
      filename.rsplit('.', 1)[1])))
  return ''



app.run(host='0.0.0.0', debug=True)