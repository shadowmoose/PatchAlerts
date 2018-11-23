from wrappers.update import Update
from games.base_class import Game
from util import loader


class Diablo3(Game):
	def __init__(self):
		super().__init__('Diablo 3', homepage='https://us.diablo3.com/en/')

	def scan(self):
		soup = loader.soup("https://us.diablo3.com/en/game/patch-notes/")
		latest = soup.find(attrs={'class': 'subpatches-nav'})
		for link in latest.find_all('a'):
			url = 'https://us.diablo3.com' + link['href']
			page = loader.soup(url)
			title = page.find(attrs={'class': 'subpatch-title'})
			desc = page.find(attrs={'class': 'sub-patches'})
			_title = title.get_text(" - ").strip().strip(' -')
			_desc = desc.get_text("\n")
			yield Update(game=self, update_name=_title, post_url=url, desc=_desc, color="#632004")


if __name__ == "__main__":
	lol = Diablo3()
	for u in lol.scan():
		print(u)
