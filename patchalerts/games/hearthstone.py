from util import loader
from wrappers.update import Update
from games.base_class import Site


class Hearthstone(Site):
	def __init__(self):
		super().__init__('Hearthstone', icon='https://i.imgur.com/fpsVoeK.png', homepage='https://playhearthstone.com/')

	def scan(self):
		soup = loader.soup("https://us.battle.net/forums/en/hearthstone/22814011/")
		table = soup.find(attrs={"class": 'Forum-ForumTopicList'})
		elems = table.find_all(attrs={'class': 'ForumTopic'})
		for elem in elems:
			dsc = elem.find(attrs={"class": 'ForumTopic-title'})
			_url = 'https://us.battle.net' + elem["href"]
			_title = dsc.text
			_desc = dsc['data-tooltip-content']
			yield Update(game=self.name, update_name=_title, post_url=_url, desc=_desc, thumb=self.icon, color="#6785c2")


if __name__ == "__main__":
	lol = Hearthstone()
	for u in lol.scan():
		print(u)
