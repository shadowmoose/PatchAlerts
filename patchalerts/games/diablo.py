from bs4 import BeautifulSoup
import requests
from wrappers.update import Update
from games.site_class import Site


class Diablo3(Site):
	def __init__(self):
		super().__init__('Diablo 3', icon='https://i.imgur.com/C9cNY2O.png', homepage='https://us.diablo3.com/en/')

	def scan(self):
		soup = BeautifulSoup(requests.get("https://us.diablo3.com/en/game/patch-notes/").text, "html.parser")
		latest = soup.find(attrs={'class': 'subpatches-nav'})
		for link in latest.find_all('a'):
			url = 'https://us.diablo3.com' + link['href']
			page = BeautifulSoup(requests.get(url).text, "html.parser")
			title = page.find(attrs={'class': 'subpatch-title'})
			desc = page.find(attrs={'class': 'sub-patches'})
			_title = title.get_text(" - ").strip().strip(' -')
			_desc = desc.get_text("\n").replace('\n\n', '\n').replace('\n\n', '\n')
			yield Update(game=self.name, update_name=_title, post_url=url, desc=_desc, thumb=self.icon, color="#632004")


if __name__ == "__main__":
	lol = Diablo3()
	for u in lol.scan():
		print(u)
