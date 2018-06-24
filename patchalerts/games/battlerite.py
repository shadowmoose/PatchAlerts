from wrappers.update import Update
from games.base_class import Site
from util import loader


class Battlerite(Site):
	def __init__(self):
		super().__init__('Battlerite', icon='https://i.imgur.com/dDIezWP.png', homepage='https://www.battlerite.com/')

	def scan(self):
		soup = loader.soup("https://blog.battlerite.com/category/updates/")
		elems = soup.find_all('article', id=lambda x: x and 'post' in x.lower())
		for elem in elems:
			link = elem.find('a')
			img = elem.find('img')
			dsc = elem.find(attrs={"class": 'entry-content'})
			_url = link["href"]
			_title = link.text
			_img = img['src']
			_desc = dsc.text
			yield Update(game=self.name, update_name=_title, post_url=_url, desc=_desc, image=_img, thumb=self.icon)

