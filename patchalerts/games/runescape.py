from util import loader
from wrappers.update import Update
from games.base_class import Game


class Runescape(Game):
	def __init__(self):
		super().__init__('Runescape', homepage='https://runescape.com/')

	def scan(self):
		data = loader.json("http://services.runescape.com/m=news/latestNews.json?cat=1")['newsItems']
		for p in data:
			_title = p['title']
			_url = p['link']
			_desc = p['summary']
			_img = p['summaryImageLink']
			yield Update(game=self, update_name=_title, post_url=_url, desc=_desc, color='#f8ca40', image=_img)


if __name__ == "__main__":
	lol = Runescape()
	for u in lol.scan():
		print(u)
