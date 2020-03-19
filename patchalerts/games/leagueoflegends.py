from util import loader
from wrappers.update import Update
from games.base_class import Game


class LeagueOfLegends(Game):
	def __init__(self):
		super().__init__('League of Legends', homepage='https://leagueoflegends.com/')

	def scan(self):
		soup = loader.soup("https://na.leagueoflegends.com/en/news/game-updates/patch")
		elems = soup.find_all('article')
		for elem in elems:
			link = elem.parent
			img = elem.find('img')
			ttl = elem.find('h2')
			_url = 'https://na.leagueoflegends.com' + link["href"]
			_title = ttl.text
			_img = img['src']
			_desc = 'Click here to read more!'
			yield Update(game=self, update_name=_title, post_url=_url, desc=_desc, image=_img, color="#e6ac00")


if __name__ == "__main__":
	lol = LeagueOfLegends()
	for u in lol.scan():
		print(u)
