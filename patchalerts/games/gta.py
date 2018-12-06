from util import loader
from wrappers.update import Update
from games.base_class import Game


class GTA5(Game):
	def __init__(self):
		super().__init__('Grand Theft Auto 5', homepage='https://www.rockstargames.com/V/')

	def scan(self):
		dat = loader.json(
			'https://www.rockstargames.com/newswire/tags.json?tags=591&page=1')
		posts = dat['posts']
		for a in posts:
			_title = loader.direct_soup(a['title']).get_text()
			_url = a['link']
			_desc = loader.direct_soup(a['blurb']).get_text()
			_image = None
			if 'preview_images_parsed' in a and 'featured' in a['preview_images_parsed']:
				_image = a['preview_images_parsed']['featured']['src']
			yield Update(game=self, update_name=_title, post_url=_url, desc=_desc, color="#588622", image=_image)


if __name__ == "__main__":
	lol = GTA5()
	for u in lol.scan():
		print(u)
