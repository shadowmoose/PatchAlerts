from util import loader
import urllib.parse
from wrappers.update import Update
from games.base_class import Site


class WorldOfTanks(Site):
	def __init__(self):
		super().__init__('World of Tanks', icon='https://i.imgur.com/eyYwEqS.png', homepage='https://worldoftanks.com')

	def scan(self):
		soup = loader.soup("https://worldoftanks.com/en/content/docs/release_notes/")
		latest = soup.find(attrs={'class': 'article-wrapper'})
		for box in latest.find_all(attrs={'class': 'spoiler'}):
			title = box.find('h2')
			desc = box.find(attrs={'class': 'spoiler_content'})
			_title = title.get_text(" - ").strip().strip(' -')
			_desc = desc.get_text("\n")
			_url = 'https://worldoftanks.com/en/content/docs/release_notes/#%s' % urllib.parse.quote(_title)
			yield Update(game=self.name, update_name=_title, post_url=_url, desc=_desc, thumb=self.icon, color="#632004")


if __name__ == "__main__":
	lol = WorldOfTanks()
	for u in lol.scan():
		print(u)
