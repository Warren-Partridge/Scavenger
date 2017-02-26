from flask import Flask
from run import getObjective, imageRec, checkIfPlayerIsGoodAtVideoGames
from camera import takePicture

app = Flask(__name__)

currentObjective = getObjective("objectives.txt")
points = 0

@app.route('/')
def index():
    print(currentObjective)
    print(str(currentObjective))
    msg = "Welcome to Scavenger! You have " + points + " points right now. Go take a picture of a " +\
          str(currentObjective) + " to get your first point."

    return '<html>'+msg+'<br><a href="/take">Take picture!</a>'

@app.route('/take')
def take():
    msg = 'Picture is going to be taken' 
    takePicture()
    imageRecData = imageRec(None)
    if(checkIfPlayerIsGoodAtVideoGames(imageRecData[1], currentObjective) == True):
        points += 1
        msg = "Nice " + currentObjective + " pic! Quality photography. " +\
            "You got 1 point, making your new score " + str(points) + "."
        currentObjective = getObjective("objectives.txt")
        msg += "Now find something new; take a picture of a " + currentObjective + "!"
        
    return '<html><br><a href="/take">Take picture!</a>'+msg

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
