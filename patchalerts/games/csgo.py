from bs4 import BeautifulSoup
import requests
from wrappers.update import Update
from games.base_class import Site


class CSGO(Site):
	def __init__(self):
		super().__init__('CS:GO', icon='https://i.imgur.com/wlhfzUT.png', homepage='http://blog.counter-strike.net/')

	def scan(self):
		soup = BeautifulSoup(requests.get("http://blog.counter-strike.net/index.php/category/updates/").text, "html.parser")
		elems = soup.find_all(attrs={'class': 'inner_post'})
		for elem in elems:
			link = elem.find('a')
			_url = link["href"]
			_title = link.text
			_desc = elem.find('p', attrs={'class': None}).text
			yield Update(game=self.name, update_name=_title, post_url=_url, desc=_desc, thumb=self.icon, color="#2f2217")


if __name__ == "__main__":
	lol = CSGO()
	for u in lol.scan():
		print(u)
