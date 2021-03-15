from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP

# Get Emotion From The Facial Recognition Model
emotion = 'anger'


def predict(emotion):
    emotion = emotion.capitalize()
    global urlhere
    if(emotion == "Anger"):
        urlhere = 'https://www.imdb.com/search/title/?genres=family&title_type=feature&sort=moviemeter, asc'

    elif(emotion == "Disgust"):
        urlhere = 'https://www.imdb.com/search/title/?genres=musical&title_type=feature&sort=moviemeter, asc'

    elif(emotion == "Fear"):
        urlhere = 'https://www.imdb.com/search/title/?genres=sport&title_type=feature&sort=moviemeter, asc'

    elif(emotion == "Happy"):
        urlhere = 'https://www.imdb.com/search/title/?genres=thriller&title_type=feature&sort=moviemeter, asc'

    elif(emotion == "Neutral"):
        urlhere = 'https://www.imdb.com/search/title/?genres=western&title_type=feature&sort=moviemeter, asc'

    elif(emotion == "Sad"):
        urlhere = 'https://www.imdb.com/search/title/?genres=drama&title_type=feature&sort=moviemeter, asc'

    elif(emotion == "Surprised"):
        urlhere = 'https://www.imdb.com/search/title/?genres=film-noir&title_type=feature&sort=moviemeter, asc'

    response = HTTP.get(urlhere)
    data = response.text

    soup = SOUP(data, 'lxml')

    for div in soup.findAll('div', attrs={'class': 'lister-item-content'}):

        link = (div.find('a')['href'])

        title = (div.find('a').contents[0])

        print(title, "https://www.imdb.com" + link)


predict(emotion)
