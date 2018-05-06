from bs4 import BeautifulSoup
import requests
from wrappers.update import Update
from games.site_class import Site


class Battlerite(Site):
	def __init__(self):
		super().__init__('Battlerite', icon='https://i.imgur.com/dDIezWP.png', homepage='https://www.battlerite.com/')

	def scan(self):
		soup = BeautifulSoup(requests.get("https://blog.battlerite.com/category/updates/").text, "html.parser")
		elems = soup.find_all('article', id=lambda x: x and 'post' in x.lower())
		for elem in elems:
			link = elem.find('a')
			img = elem.find('img')
			dsc = elem.find(attrs={"class": 'entry-content'})
			_url = link["href"]
			_title = link.text
			_img = img['src']
			_desc = dsc.text
			yield Update(game=self.name, update_name=_title, post_url=_url, desc=_desc, image=_img)

