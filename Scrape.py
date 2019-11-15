import requests
from bs4 import BeautifulSoup
from googlesearch import search
features="html.parser"

class Lyrics():
    lyrics = ""

    def __init__(self, details):
        self.details = details

    def getLyrics(self):
            for x in search(details, tld="co.in", lang='en', start=0, stop=1):
                    site = x
            req = requests.get(site)
            soup = BeautifulSoup(req.content, features)
            lyrics = ""
            for link in soup.find_all("p"):
                lyrics += link.text
            print(lyrics)

continueProg = True

while continueProg:
        print("1. Get a song")
        print("2. Exit")

        print("Enter an option: ")
        option = int(input())

        if option == 1:
                print("Please enter the name of the song, and the artist, followed by enter: ")
                details = " genius lyrics" + input()
                scrape = Lyrics(details)
                print("Lyrics: ")
                print("")
                scrape.getLyrics()
                print("Press enter to continue....")
                input()

        elif option == 2:
                print("Later")
                continueProg = False
                exit()

