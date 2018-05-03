from bs4 import BeautifulSoup
import requests
from wrappers.updates import Update
from sites.site_class import Site


class Warframe(Site):
	def __init__(self):
		super().__init__('Warframe')

	def scan(self):
		soup = BeautifulSoup(requests.get("https://forums.warframe.com/forum/3-pc-update-build-notes/").text, "html.parser")
		table = soup.find(attrs={"class": 'cTopicList'})
		elems = table.find_all('li', attrs={'class': 'ipsDataItem'})
		for elem in elems:
			link = elem.find('a')
			_url = link["href"]
			_title = link.text
			_desc = link.text
			_thumb = 'http://i.imgur.com/lh5YKoc.png'
			yield Update(game=self.name, update_name=_title, post_url=_url, u_desc=_desc, thumb=_thumb)


if __name__ == "__main__":
	lol = Warframe()
	for u in lol.scan():
		print(u)
