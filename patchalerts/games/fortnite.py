from util import loader
from wrappers.update import Update
from games.base_class import Game


class Fortnite(Game):
	def __init__(self):
		super().__init__("Fortnite", homepage='https://www.epicgames.com/fortnite/')

	def scan(self):
		soup = loader.soup("https://www.epicgames.com/fortnite/en-US/patch-notes/")  # Follow redirect to latest.
		_title = soup.find(attrs={'property': "og:title"})['content']
		_desc = soup.find(attrs={'class': "patch-notes-text"}).get_text('\n')
		_img = soup.find(attrs={'property': "og:image"})['content']
		_url = loader.get_redirect()
		yield Update(game=self, update_name=_title, post_url=_url, desc=_desc, image=_img, color="#1c237a")


if __name__ == "__main__":
	lol = Fortnite()
	for u in lol.scan():
		print(u)
