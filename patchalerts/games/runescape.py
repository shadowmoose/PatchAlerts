import requests
from wrappers.update import Update
from games.base_class import Site


class Runescape(Site):
	def __init__(self):
		super().__init__('Runescape', icon='https://i.imgur.com/QTqit7h.png', homepage='https://runescape.com/')

	def scan(self):
		data = requests.get("http://services.runescape.com/m=news/latestNews.json?cat=1").json()['newsItems']
		for p in data:
			_title = p['title']
			_url = p['link']
			_desc = p['summary']
			_img = p['summaryImageLink']
			yield Update(game=self.name, update_name=_title, post_url=_url, desc=_desc, thumb=self.icon, color='#f8ca40',
						image=_img)


if __name__ == "__main__":
	lol = Runescape()
	for u in lol.scan():
		print(u)
