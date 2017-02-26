import http.client, urllib.request, urllib.parse, urllib.error, base64
import camera
import json
import random

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '3ee551c38ccc452e909f6b4044884372',
}

params = urllib.parse.urlencode({
    # Request parameters
    'visualFeatures': 'Description',
    #'details': '{string}',
    'language': 'en',
})

pic = open('image.jpg', 'rb').read()

def imageRec():
    #formattedUrl = '{"url":"' + url + '"}'
    #formattedUrl = "'" + formattedUrl + "'"
    #print(formattedUrl)
    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, pic, headers)
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        data_json = json.loads(data)
        data_json_tags = data_json["description"]["tags"]
        data_json_descriptiontext = data_json["description"]["captions"][0]["text"]

        #print(data_json_descriptiontext)
        #print("");
        #print(data_json_tags)
        conn.close()
        return data_json_descriptiontext, data_json_tags
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def getObjective(afile):
    return random.choice(list(open(afile))).rstrip()

def checkIfPlayerIsGoodAtVideoGames(tags, objective):
    if(objective in tags):
        return True
    return False

def main():
    currentObjective = getObjective("objectives.txt")
    print("Welcome to Scavenger! You have 0 points right now. Go take a picture of a " +\
          currentObjective + " to get your first point.")
    points = 0;
    failCount = 0;
    while True:
        i = input() # hacky way of waiting for user interaction
        camera.takePicture()
        imageRecData = imageRec()
        
        if(checkIfPlayerIsGoodAtVideoGames(imageRecData[1], currentObjective) == True):
            points+= 1
            print("Nice " + currentObjective + " pic! Quality photography. " +\
                  "You got 1 point, making your new score " + str(points) + ".")
            currentObjective = getObjective("objectives.txt")
            print("Now find something new; take a picture of a " + currentObjective + "!")
        elif(failCount > 2):
            currentObjective = getObjective("objectives.txt")
            failCount = 0
            print("That just looks like " + imageRecData[0] + " to me. " +\
                  "Here, I'll give you a new item: take a picture of a " + currentObjective + "!")
        else:
            print("Hmm, that doesn't look like a " + currentObjective + " to me. " +\
                  "I see " + imageRecData[0] + ".")
            failCount+= 1
            # Continue looping


main()
