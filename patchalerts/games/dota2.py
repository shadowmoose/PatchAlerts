from bs4 import BeautifulSoup
import requests
from wrappers.update import Update
from games.base_class import Site


class DOTA2(Site):
	def __init__(self):
		super().__init__("DOTA 2", 'https://i.imgur.com/h1ExdFI.png', homepage='http://www.dota2.com')

	def scan(self):
		found = []  # Gotta dedupe these, because the devs post everything twice.
		resp = requests.get("http://www.dota2.com/news/updates/")
		soup = BeautifulSoup(resp.text, "html.parser")
		bod = soup.find(attrs={'id': 'mainLoop'})
		for p in bod.find_all("div", id=lambda i: i and "post-" in i):
			title = p.find(attrs={'class': 'entry-title'})
			link = title.find('a')
			desc = p.find(attrs={'class': 'entry-content'})
			_url = link['href']
			_title = title.text
			_desc = desc.get_text("\n\n")  # Converts <br> tags to newlines.
			if _url not in found:
				found.append(_url)
				yield Update(game=self.name, update_name=_title, post_url=_url, desc=_desc, thumb=self.icon, color="#656565")


if __name__ == "__main__":
	lol = DOTA2()
	for u in lol.scan():
		print(u)
