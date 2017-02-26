from flask import Flask
from run import getObjective, imageRec, checkIfPlayerIsGoodAtVideoGames
from camera import takePicture

app = Flask(__name__)

currentObjective = getObjective("objectives.txt")
points = 0
failCount = 0

@app.route('/')
def index():
    global currentObjective
    global points
    print(currentObjective)
    print(str(currentObjective))
    msg = "Welcome to Scavenger! You have " + str(points) + " points right now. Go take a picture of a " +\
          str(currentObjective) + " to get your first point."

    return '<html>'+msg+'<br><a href="/take">Take picture!</a>'

@app.route('/take')
def take():
    global currentObjective
    global points
    global failCount
    msg = 'Picture is going to be taken' 
    takePicture()
    imageRecData = imageRec(None)
    if(checkIfPlayerIsGoodAtVideoGames(imageRecData[1], currentObjective) == True):
        points += 1
        msg = "Nice " + currentObjective + " pic! Quality photography. " +\
            "You got 1 point, making your new score " + str(points) + "."
        currentObjective = getObjective("objectives.txt")
        msg += "Now find something new; take a picture of a " + currentObjective + "!"
    elif(failCount > 2):
        currentObjective = getObjective("objectives.txt")
        failCount = 0
        msg = "That just looks like " + imageRecData[0] + " to me. " +\
            "Here, I'll give you a new item: take a picture of a " + currentObjective + "."
    else:
        msg = "Hmm, that doesn't look like a " + currentObjective + " to me. " +\
            "I see " + imageRecData[0] + ". Your current score is " + str(points)
        failCount += 1

        
    return '<html><br><a href="/take">Take picture!</a>'+msg

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
