from bs4 import BeautifulSoup
import requests
from wrappers.update import Update
from games.site_class import Site


class HuntShowdown(Site):
	def __init__(self):
		super().__init__('Hunt: Showdown', icon='https://i.imgur.com/SnQ6cRD.png', homepage='https://www.huntshowdown.com/')

	def scan(self):
		soup = BeautifulSoup(requests.get("https://www.huntshowdown.com/news/tagged/news").text, "html.parser")
		sect = soup.find(attrs={'class': 'news-feature'})
		for elem in sect.find_all(attrs={"class": 'col'}):
			link = elem.find('a')
			img = elem.find('img')
			dsc = elem.find('p')
			ttl = elem.find('h3')
			_url = 'https://www.huntshowdown.com' + link["href"]
			_title = ttl.text
			_img = 'https://www.huntshowdown.com' + img['src']
			_desc = dsc.text
			yield Update(game=self.name, update_name=_title, post_url=_url, desc=_desc, thumb=_img, color="#cc0000")


if __name__ == "__main__":
	lol = HuntShowdown()
	for u in lol.scan():
		print(u)
