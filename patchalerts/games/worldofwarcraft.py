import html
from util import loader
from wrappers.update import Update
from games.base_class import Game


class WorldOfWarcraft(Game):
	def __init__(self):
		super().__init__('World of Warcraft', homepage='https://worldofwarcraft.com/')

	def scan(self):
		soup = loader.soup("http://us.battle.net/wow/en/game/patch-notes/")
		for item in soup.find_all(attrs={'class': 'NewsBlog'}):
			link = item.find('a')
			url = 'http://us.battle.net' + link['href']
			title = item.find(attrs={'class': 'NewsBlog-title'})
			desc = item.find(attrs={'class': 'NewsBlog-desc'})
			_title = title.get_text(" - ").strip().strip(' -')
			_desc = html.unescape(desc.get_text("\n").replace('\u200b', '').strip())
			yield Update(game=self, update_name=_title, post_url=url, desc=_desc, color="#78ab60")


if __name__ == "__main__":
	lol = WorldOfWarcraft()
	for u in lol.scan():
		print(u)
