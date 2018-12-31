import os

from datetime import datetime

from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

ALLOWED_PICTURE_FORMATS = ['jpg', 'png',]

@app.route('/upload_picture/<project_name>', methods=['POST'])
def receive_and_save_file(project_name):

  project_path = os.path.join(os.curdir, 'projects', project_name)
  if not os.path.exists(project_path):
    os.mkdir(project_path)

  if request.method == 'POST':
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('projects', project_name, '{}_{}.{}'.format(filename.split('.')[0],
                                                                       str(datetime.now()),
                                                                       filename.rsplit('.', 1)[1])))

  return ''

@app.route('/create-time-lapse/<project_name>', methods=['POST'])
def create_time_lapse(project_name):

  project_path = os.path.join(os.curdir, 'projects', project_name)

  # Get pictures in folder
  pictures = [x for x in os.listdir(project_path) if x.rsplit('.', 1)[1].lower() in ALLOWED_PICTURE_FORMATS]

  print('Creating time-lapse with {} pictures. Filename: {}.mp4'.format(len(pictures), project_name))
  os.system("ffmpeg -r 5 -pattern_type glob -i '{}/*.jpg' -s hd1080 -vcodec libx264 {}.mp4".format(
          project_path,
          project_name))

  return ''

app.run(host='0.0.0.0', debug=True)