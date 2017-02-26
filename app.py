from flask import Flask
from run import getObjective, imageRec
from camera import takePicture

app = Flask(__name__)

@app.route('/')
def index():
    msg = "Welcome to Scavenger! You have 0 points right now. Go take a picture of a " +\
          getObjective("/home/pi/Desktop/Scavenger/objectives.txt") + " to get your first point."
    return '<html>'+msg+'<br><a href="/take">Take picture!</a>'

@app.route('/take')
def take():
    msg = 'Picture is going to be taken' 
    takePicture()
    imageRec(None)
    msg = msg + '<script>document.location="/"</script>'
    return msg 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
