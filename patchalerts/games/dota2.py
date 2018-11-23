from util import loader
from wrappers.update import Update
from games.base_class import Game


class DOTA2(Game):
	def __init__(self):
		super().__init__("DOTA 2", homepage='http://www.dota2.com')

	def scan(self):
		found = []  # Gotta dedupe these, because the devs post everything twice.
		soup = loader.soup("http://www.dota2.com/news/updates/")
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
				yield Update(game=self, update_name=_title, post_url=_url, desc=_desc, color="#656565")


if __name__ == "__main__":
	lol = DOTA2()
	for u in lol.scan():
		print(u)
