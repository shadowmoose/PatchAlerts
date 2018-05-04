from bs4 import BeautifulSoup
import requests
from wrappers.updates import Update
from sites.site_class import Site


class CSGO(Site):
	def __init__(self):
		super().__init__('Counter-Strike: Global Offensive', icon='https://i.imgur.com/wlhfzUT.png')

	def scan(self):
		soup = BeautifulSoup(requests.get("http://blog.counter-strike.net/index.php/category/updates/").text, "html.parser")
		elems = soup.find_all(attrs={'class': 'inner_post'})
		for elem in elems:
			link = elem.find('a')
			_url = link["href"]
			_title = link.text
			_desc = elem.find('p', attrs={'class': None}).text
			yield Update(game=self.name, update_name=_title, post_url=_url, desc=_desc, thumb=self.icon, color="#6785c2")


if __name__ == "__main__":
	lol = CSGO()
	for u in lol.scan():
		print(u)
