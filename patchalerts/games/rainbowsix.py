from util import loader
from wrappers.update import Update
from games.base_class import Game


class RainbowSix(Game):
	def __init__(self):
		super().__init__('Rainbow Six Siege', homepage='https://rainbow6.ubisoft.com/siege/en-us/')

	def scan(self):
		data = loader.json("https://www.ubisoft.com/api/updates/items?categoriesFilter=game-updates"
							"&limit=6"
							"&mediaFilter=all"
							"&skip=0"
							"&startIndex=undefined"
							"&locale=en-us"
							"&fallbackLocale=en-us"
							"&tags=BR-rainbow-six%20GA-siege")['items']
		for p in data:
			_img = p['thumbnail']['url']
			_title = p['title']
			_desc = p['abstract']
			_url = 'https://www.ubisoft.com/en-us/game/rainbow-six/siege' + p['button']['buttonUrl']
			yield Update(game=self, update_name=_title, post_url=_url, desc=_desc, color='#333740', image=_img)


if __name__ == "__main__":
	lol = RainbowSix()
	for u in lol.scan():
		print(u)
