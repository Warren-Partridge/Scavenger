import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import random

headers = {
    # Request headers
    #'Content-Type': 'application/json',
    'Content-Type': 'application/octet-stream', 
    'Ocp-Apim-Subscription-Key': '3ee551c38ccc452e909f6b4044884372',
}

params = urllib.parse.urlencode({
    # Request parameters
    'visualFeatures': 'Description',
    #'details': '{string}',
    'language': 'en',
})

def imageRec(url):
    #formattedUrl = '{"url":"' + url + '"}'
    #formattedUrl = "'" + formattedUrl + "'"
    #print(formattedUrl)
    try:
        data = None
        with open('/home/pi/Desktop/image.jpg','rb') as f:
            data = f.read()

        print('Here A')
 
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
#        conn.request("POST", "/vision/v1.0/analyze?%s" % params, '{"url":"https://www.what-dog.net/Images/faces2/scroll0015.jpg"}', headers)
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, data, headers)

        print('Here B')
        
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
        print (e)
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    return data_json_tags 

def getObjective(afile):
    return random.choice(list(open(afile)))


def main2():
    print("Welcome to Scavenger! You have 0 points right now. Go take a picture of a " +\
          getObjective("/home/pi/Desktop/Scavenger/objectives.txt") + " to get your first point.")
    imageRec("https://www.what-dog.net/Images/faces2/scroll0015.jpg")
    #while True:
        #i = input() # hacky way of waiting for user interaction
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
            
def main():
    print('run.main')

main()
