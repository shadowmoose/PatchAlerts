from wrappers.update import Update
from games.base_class import Game
from util import loader


class PUBG(Game):
	def __init__(self):
		super().__init__("PUBG", homepage='https://playbattlegrounds.com/')

	def scan(self):
		soup = loader.soup("https://www.pubg.com/category/patch-notes/")
		table = soup.find(attrs={"class": "l-gutters"})
		elems = table.find_all(attrs={'class': 'l-gutters__item'})
		for elem in elems:
			link = elem.find('a')
			img = elem.find('img')
			dsc = elem.find('p')  # Yes, they actually spelled 'description' wrong.
			ttl = elem.find('h2')
			_url = 'https://playbattlegrounds.com' + link["href"]
			_title = ttl.text
			_img = img['src'] if img else None
			_desc = dsc.text + '...'
			yield Update(game=self, update_name=_title, post_url=_url, desc=_desc, image=_img, color="#bf1866")


if __name__ == "__main__":
	lol = PUBG()
	for u in lol.scan():
		print(u)
