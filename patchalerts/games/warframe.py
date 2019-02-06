from util import loader
from wrappers.update import Update
from games.base_class import Game
from util.errors import TemporarySiteException


class Warframe(Game):
	def __init__(self):
		super().__init__('Warframe', homepage='https://www.warframe.com/')

	def scan(self):
		soup = loader.soup("https://forums.warframe.com/forum/3-pc-update-build-notes/")
		table = soup.find(attrs={"class": 'cTopicList'})
		if 'ERROR: The request could not be satisfied' in soup.prettify():
			raise TemporarySiteException()
		elems = table.find_all('li', attrs={'class': 'ipsDataItem'})
		for elem in elems:
			link = elem.find('a')
			_url = link["href"]
			_title = link.text
			_desc = 'Click to read more.'
			yield Update(game=self, update_name=_title, post_url=_url, desc=_desc, color='#C0C0C0')


if __name__ == "__main__":
	lol = Warframe()
	for u in lol.scan():
		print(u)
