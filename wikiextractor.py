import requests
import json
import os.path
import sys

class User:

    def __init__(self):
        pass

    def userin():
        info = 0
        temp1 = ""
        temp2 = []

        raw_input = input("Quel lieu ? ")

        for i in raw_input:
            if info == 1:
                i = i.capitalize()
                info = 0
            if i == " ":
                i = "_"
                info = 1
            temp2.append(i)
        if temp2[0].upper() != temp2[0]:
            temp2[0] = temp2[0].capitalize()
        title = temp1.join(temp2)
        
        return title

class Separator:

    def __init__(self, title):
        self.title = title

    def splitter(self):
        entry_list = (title.split('_'))
        #print(entry_list)

    def maps_splitter(self):
        temp1 = ""
        temp2 = []

        for i in title:
            if i == "_":
                i = "+"
            temp2.append(i)
        splitted = temp1.join(temp2)

        return splitted

class Extractor:

    def __init__(self, title, splitted):
        self.title = title
        self.splitted = splitted

    def wikiextract(self):
        url = "https://fr.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "prop": "extracts",
            "titles": f"{title}",
            "explaintext": 1,
        #"exsentences": 15,
        #"rvprop": "content",
        #"rvslots": "main",
            "formatversion": "2",
            "format": "json"
        }
        req = requests.get(url, params)
        extracted = json.loads(req.content.decode('UTF-8'))
        #indent = json.dumps(extracted, indent = 4)
        #print(extracted)
        print(extracted["query"]["pages"][0]["extract"])
        #print(extracted["query"]["pages"][0]["revisions"][0]["slots"]["main"]["content"])

    def mapsextract(self):
        print(splitted)
        url = f"https://maps.googleapis.com/maps/api/geocode/json?"
        params = {
            "address": f"{splitted}",
            "key": ""
        }
        req = requests.get(url, params)
        extracted = json.loads(req.content.decode('UTF-8'))
        completeName = \
                path = os.path.join("projet7/ressources/temp/extracted.json")
        f = open(completeName, "w")
        f.write(json.dumps(extracted))
        f.close()
        #print("lat: ", extracted['results'][0]['geometry']['location']['lat'])
        #print("log: ", extracted['results'][0]['geometry']['location']['lng'])


title = User.userin()
#Extractor(title).wikiextract()
#Separator(title).splitter()
splitted = Separator(title).maps_splitter()
Extractor(title, splitted).mapsextract()