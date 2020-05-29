from util import loader
from wrappers.update import Update
from games.base_class import Game


class Overwatch(Game):
	def __init__(self):
		super().__init__("Overwatch", homepage='https://playoverwatch.com/')

	def scan(self):
		soup = loader.soup("https://playoverwatch.com/en-us/news/patch-notes/pc/")
		bod = soup.find_all(attrs={'class': 'PatchNotes-section'})
		date = soup.find(attrs={'class': 'PatchNotes-patch'})['id'].replace(' ', '')
		_title = soup.find(attrs={'class': 'PatchNotes-patchTitle'}).text
		_url = 'https://playoverwatch.com/en-us/news/patch-notes#%s' % date
		_desc = bod[1].text if len(bod) else bod[0].text
		yield Update(game=self, update_name=_title, post_url=_url, desc=_desc, color="#f99e1a")


if __name__ == "__main__":
	lol = Overwatch()
	for u in lol.scan():
		print(u)
