import http.client, urllib.request, urllib.parse, urllib.error, base64
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

        print(data_json_descriptiontext)
        print("");
        print(data_json_tags)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def getObjective(afile):
    return random.choice(list(open(afile)))


def main():
    print("Welcome to Scavenger! You have 0 points right now. Go take a picture of a " +\
          getObjective("objectives.txt") + " to get your first point.")
    imageRec()
    while True:
        i = input() # hacky way of waiting for user interaction
        # TODO: Snap a picture
        print("Snap! Pretend that I took a picture there")
        # TODO: Check if that picture matches the thing
        # If yes:
            # Award points
            # List current points
            # Maybe change objective?
        # If no:
            # Tell user what it thinks your picture is (print description text)
            # Continue looping
            

main()
