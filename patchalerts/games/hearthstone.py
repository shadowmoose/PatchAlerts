from util import loader
from wrappers.update import Update
from games.base_class import Game


class Hearthstone(Game):
	def __init__(self):
		super().__init__('Hearthstone', homepage='https://playhearthstone.com/')

	def scan(self):
		soup = loader.json('https://playhearthstone.com/en-us/api/blog/articleList/?page=1&pageSize=12&tagsList[]=patch')
		for upd in soup:
			title = upd['title']
			desc = upd['summary']
			img = 'https:' + upd['thumbnail']['url']
			url = upd['defaultUrl']
			yield Update(game=self, update_name=title, post_url=url, desc=desc, color="#6785c2", image=img)


if __name__ == "__main__":
	lol = Hearthstone()
	for u in lol.scan():
		print(u)
