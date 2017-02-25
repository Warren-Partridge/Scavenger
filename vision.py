import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import random

headers = {
    # Request headers
    'Content-Type': 'application/json',
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
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, '{"url":"https://www.what-dog.net/Images/faces2/scroll0015.jpg"}', headers)
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
    print(getObjective("objectives.txt"))
    imageRec("https://www.what-dog.net/Images/faces2/scroll0015.jpg")


main()
