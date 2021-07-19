import model
import requests

def getQuestion(catName):
    choiceID = 0
    for category in model.categories:
        if category["title"] == catName:
            choiceID = category["id"]
    response = requests.get(f'http://jservice.io/api/clues?category={choiceID}').json()
    return response[0]