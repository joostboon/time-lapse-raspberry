# time-lapse-raspberry

Simple program to create time-lapse movie with a raspberry pi.

Equipment used:
- Raspberry Pi 3 Model B+
- Raspberry Pi Camera Module V2
- Server

Software used:
- Python 3.7 (Python2.7 compatible)
    - Flask
    - raspistill

Pictures are taken with the camera module and sent to a Python Flask API on the server. After successful upload, pictures are deleted.

Once the time period is over, a command is sent to the server to create the time-lapse video.
 