from util import loader
from wrappers.update import Update
from games.base_class import Game


class HuntShowdown(Game):
	def __init__(self):
		super().__init__('Hunt: Showdown', homepage='https://www.huntshowdown.com/')

	def scan(self):
		soup = loader.soup("https://www.huntshowdown.com/news/tagged/news")
		sect = soup.find(attrs={'class': 'news-feature'})
		for elem in sect.find_all(attrs={"class": 'col'}):
			link = elem.find('a')
			img = elem.find('img')
			dsc = elem.find('p')
			ttl = elem.find('h3')
			_url = 'https://www.huntshowdown.com' + link["href"]
			_title = ttl.text
			_img = 'https://www.huntshowdown.com' + img['src']
			_desc = dsc.text
			yield Update(game=self, update_name=_title, post_url=_url, desc=_desc, color="#cc0000")


if __name__ == "__main__":
	lol = HuntShowdown()
	for u in lol.scan():
		print(u)
