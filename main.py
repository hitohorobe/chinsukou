import requests
import random

def makeword(): 
    characters = ["ち", "ん", "す", "こ", "う"]
    word = ""
    random.shuffle(characters)
    for character in characters:
        word = word + character
    
    return word

def post(keyword):
    event = 'feed'
    key = 'ここにwebhookのapi key' 
    url = 'https://maker.ifttt.com/trigger/{}/with/key/{}'.format(event, key)
    requests.post(url, data={'value1': keyword})


if __name__ == "__main__":
    keyword = makeword()
    post(keyword)
    print(keyword)
