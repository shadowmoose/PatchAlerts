from util import loader
from wrappers.update import Update
from games.base_class import Site


class GTA5(Site):
	def __init__(self):
		super().__init__('Grand Theft Auto 5', icon='https://i.imgur.com/MDpiySe.png',
						homepage='https://www.rockstargames.com/V/')

	def scan(self):
		dat = loader.json(
			'https://www.rockstargames.com/newswire/tags.json?tags=591&page=1')
		posts = dat['posts']
		for a in posts:
			_title = a['title'].split('<')[0]
			_url = a['link']
			_desc = a['blurb'].split('<')[0].replace('\n\n', '\n').replace('\n\n', '\n')
			_image = None
			if 'preview_images_parsed' in a and 'featured' in a['preview_images_parsed']:
				_image = a['preview_images_parsed']['featured']['src']
			yield Update(game=self.name, update_name=_title, post_url=_url, desc=_desc, thumb=self.icon, color="#588622", image=_image)


if __name__ == "__main__":
	lol = GTA5()
	for u in lol.scan():
		print(u)
