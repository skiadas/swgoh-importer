import requests
from webpage import WebPage

class Downloader:
	def __init__(self):
		self.baseUrl = "https://swgoh.gg"

	def get(self, url):
		r = requests.get(self.baseUrl + url)
		return WebPage(r.text)

	def getCharacterUnits(self, name):
		page = self.get("/u/" + name + "/collection")
		characterEntries = page.soup.find_all('div', class_='collection-char')
		return characterEntries

results = Downloader().getCharacterUnits("atosite")
for result in results:
	name = result.find('img', class_="char-portrait-full-img")['alt']
	imgLink = result.find('img', class_="char-portrait-full-img")['data-src']
	charLink = result.find('a', class_="char-portrait-full-link")['href']
	print(name)
	print(imgLink)
	print(charLink)