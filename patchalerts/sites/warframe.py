from bs4 import BeautifulSoup
import requests
from wrappers.update import Update
from sites.site_class import Site


class Warframe(Site):
	def __init__(self):
		super().__init__('Warframe', icon='http://i.imgur.com/lh5YKoc.png')

	def scan(self):
		soup = BeautifulSoup(requests.get("https://forums.warframe.com/forum/3-pc-update-build-notes/").text, "html.parser")
		table = soup.find(attrs={"class": 'cTopicList'})
		elems = table.find_all('li', attrs={'class': 'ipsDataItem'})
		for elem in elems:
			link = elem.find('a')
			_url = link["href"]
			_title = link.text
			_desc = link.text
			yield Update(game=self.name, update_name=_title, post_url=_url, desc=_desc, thumb=self.icon, color='#C0C0C0')


if __name__ == "__main__":
	lol = Warframe()
	for u in lol.scan():
		print(u)
