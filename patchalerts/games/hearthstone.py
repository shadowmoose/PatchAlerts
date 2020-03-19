from util import loader
from wrappers.update import Update
from games.base_class import Game


class Hearthstone(Game):
	def __init__(self):
		super().__init__('Hearthstone', homepage='https://playhearthstone.com/')

	def scan(self):
		soup = loader.soup("https://playhearthstone.com/en-us/blog//infinite?page=1&articleType=blog")
		print('Soup:', soup)
		elems = soup.find_all('li')
		for elem in elems:
			a = elem.find(attrs={"class": "article-title"}).find(attrs={'class': 'media--link'})
			dsc = elem.find(attrs={"class": 'article-summary'})
			_url = 'https://playhearthstone.com' + a["href"]
			_title = a.text
			_desc = dsc.text
			_img = 'https:' + elem.find('img')['data-src']
			yield Update(game=self, update_name=_title, post_url=_url, desc=_desc, color="#6785c2", image=_img)


if __name__ == "__main__":
	lol = Hearthstone()
	for u in lol.scan():
		print(u)
