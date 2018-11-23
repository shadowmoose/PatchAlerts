from util import loader
from wrappers.update import Update
from games.base_class import Game


class WorldOfWarcraft(Game):
	def __init__(self):
		super().__init__('World of Warcraft', homepage='https://worldofwarcraft.com/')

	def scan(self):
		soup = loader.soup("http://us.battle.net/wow/en/game/patch-notes/")
		latest = soup.find(attrs={'class': 'subpatches-nav'})
		for link in latest.find_all('a'):
			if 'overview' in link.text.lower():
				continue
			url = 'http://us.battle.net' + link['href']
			page = loader.soup(url)
			title = page.find(attrs={'class': 'subpatch-title'})
			desc = page.find(attrs={'class': 'sub-patches'})
			_title = title.get_text(" - ").strip().strip(' -')
			_desc = desc.get_text("\n")
			yield Update(game=self, update_name=_title, post_url=url, desc=_desc, color="#78ab60")


if __name__ == "__main__":
	lol = WorldOfWarcraft()
	for u in lol.scan():
		print(u)
