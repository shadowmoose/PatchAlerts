from util import loader
from wrappers.update import Update
from games.base_class import Site


class Overwatch(Site):
	def __init__(self):
		super().__init__("Overwatch", 'https://i.imgur.com/Wp2Xlvw.png', homepage='https://playoverwatch.com/')

	def scan(self):
		soup = loader.soup("https://playoverwatch.com/en-us/news/patch-notes/pc/")
		bod = soup.find(attrs={'class': 'patch-notes-patch'})
		link = soup.find(attrs={'class': 'PatchNotesSideNav'}).find('a')

		_title = link.find('h3').text
		_url = 'https://playoverwatch.com/en-us/game/patch-notes/pc/' + link['href']  # First link in sidebar.
		_desc = bod.text
		yield Update(game=self.name, update_name=_title, post_url=_url, desc=_desc, thumb=self.icon, color="#f99e1a")


if __name__ == "__main__":
	lol = Overwatch()
	for u in lol.scan():
		print(u)
