from bs4 import BeautifulSoup

class WebPage:
	def __init__(self, text):
		res = BeautifulSoup(text, "html.parser")
		self.soup = res 

	def __str__(self):
		return self.soup.prettify()