from wrappers.update import Update
from games.base_class import Game
from util import loader


class DBD(Game):
	def __init__(self):
		super().__init__('Dead By Daylight', homepage='http://deadbydaylight.com')

	def scan(self):
		soup = loader.soup("http://archive.deadbydaylight.com/posts/category/patch-notes/")
		elems = soup.find_all('article')
		for elem in elems:
			link = elem.find('a')
			dsc = elem.find_all('p')[1]
			_url = link["href"]
			_title = link['title']
			_desc = dsc.text
			yield Update(game=self, update_name=_title, post_url=_url, desc=_desc, color="#6785c2")


if __name__ == "__main__":
	lol = DBD()
	for u in lol.scan():
		print(u)
